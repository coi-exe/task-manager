from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SimpleUserCreationForm, TaskForm
from .models import Task
from django.shortcuts import redirect

def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = SimpleUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully! Welcome!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = SimpleUserCreationForm()
    
    return render(request, 'todo_app/register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'todo_app/login.html')

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('login')

@login_required
def dashboard_view(request):
    tasks = Task.objects.filter(user=request.user)
    
    # Filter tasks based on status
    status_filter = request.GET.get('status')
    if status_filter:
        tasks = tasks.filter(status=status_filter)
    
    # Search functionality
    search_query = request.GET.get('search')
    if search_query:
        tasks = tasks.filter(title__icontains=search_query)
    
    context = {
        'tasks': tasks,
        'total_tasks': tasks.count(),
        'pending_tasks': tasks.filter(status='pending').count(),
        'completed_tasks': tasks.filter(status='completed').count(),
    }
    return render(request, 'todo_app/dashboard.html', context)

@login_required
def create_task_view(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, 'Task created successfully!')
            return redirect('dashboard')
    else:
        form = TaskForm()
    
    return render(request, 'todo_app/task_form.html', {'form': form, 'title': 'Create Task'})

@login_required
def update_task_view(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully!')
            return redirect('dashboard')
    else:
        form = TaskForm(instance=task)
    
    return render(request, 'todo_app/task_form.html', {'form': form, 'title': 'Update Task'})

@login_required
def delete_task_view(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Task deleted successfully!')
        return redirect('dashboard')
    
    return render(request, 'todo_app/delete_confirm.html', {'task': task})

@login_required
def mark_task_complete(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.status = 'completed'
    task.save()
    messages.success(request, 'Task marked as completed!')
    return redirect('dashboard')

def root_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return redirect('login')
    
def home_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'todo_app/home.html')