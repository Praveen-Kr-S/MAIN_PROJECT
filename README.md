# Django Inventory & Order Management System

## Project Overview
This project is a web-based **Inventory and Order Management System** developed using the Django framework.  
It helps manage product inventory, customer orders, and user authentication through a structured web interface.

The application follows Django's **MVT (Model–View–Template)** architecture and uses **MySQL** as the backend database.  
The system also implements **session-based authentication and authorization** for secure user access.

---

## Technologies Used

- Python
- Django
- MySQL
- HTML
- CSS
- Bootstrap
- JavaScript

---

## Project Architecture

This project follows Django's **MVT Architecture**.

### Model
Defines database structure and business logic.

### View
Handles request processing and returns responses.

### Template
Responsible for displaying data in the frontend UI.

---

## Project Structure

```
MAIN_PROJECT
│
├── Dj_project/           # Main Django project configuration
│   ├── settings.py
│   ├── urls.py
│   └── asgi.py / wsgi.py
│
├── authentication/       # User authentication module
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── Inventory/            # Inventory management module
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── OrderManagement/      # Order management module
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── Frontend/             # Frontend templates
│
├── static/               # Static files (CSS, JS, Images)
│
├── manage.py
└── .gitignore
```

---

## Key Features

- User Registration and Login
- Session-based Authentication
- Authorization for protected pages
- Inventory Management System
- Order Management System
- Responsive UI using Bootstrap
- Django Admin Panel
- Dynamic Web Pages using Django Templates
- MySQL Database Integration

---

## Database

Database used in this project:

**MySQL**

Django is connected to MySQL through configuration in:

```
settings.py
```

---

## Authentication & Authorization

The system uses **Django session-based authentication**.

Features include:

- Secure user login
- Session management
- Access control for authenticated users
- Protected views using Django authentication system

---

## How to Run the Project

### 1 Install Dependencies

```
pip install -r requirements.txt
```

### 2 Apply Migrations

```
python manage.py makemigrations
python manage.py migrate
```

### 3 Run the Server

```
python manage.py runserver
```

### 4 Open in Browser

```
http://127.0.0.1:8000/
```

---

## Future Improvements

- REST API integration using Django REST Framework
- Advanced analytics dashboard
- Role-based user permissions
- Reporting and data export features

---

## Author

Praveen Kumar S  

Python Full Stack Developer  
Django | Python | Bootstrap | MySQL
