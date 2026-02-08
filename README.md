# To-Do Application

A fully functional To-Do web application built with Django, Bootstrap 5, and SQLite.

## Features

- ✅ User authentication (Register/Login/Logout)
- ✅ Create, Read, Update, Delete (CRUD) tasks
- ✅ Task status tracking (Pending, In Progress, Completed)
- ✅ Due dates and deadlines
- ✅ Search and filter tasks
- ✅ Responsive design with Bootstrap 5
- ✅ Beautiful dashboard with statistics
- ✅ Overdue task highlighting

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/coi-exe/task-manager.git
cd django-todo-app
```
### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply migrations
```bash
python manage.py migrate
```

### 5. Create a superuser (optional)
```bash
python manage.py createsuperuser
```

### 6. Run the development server
```bash
python manage.py runserver
```

### 7. Open in browser
Visit http://127.0.0.1:8000/
