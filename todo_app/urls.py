from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('tasks/create/', views.create_task_view, name='create_task'),
    path('tasks/<int:task_id>/update/', views.update_task_view, name='update_task'),
    path('tasks/<int:task_id>/delete/', views.delete_task_view, name='delete_task'),
    path('tasks/<int:task_id>/complete/', views.mark_task_complete, name='complete_task'),
]