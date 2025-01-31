# SLATE API

This is a Django project that implements a JWT-based authentication system with the following endpoints:
- **Signup** (`POST api/signup/`)
- **Login** (`POST api/login/`)
- **Refresh Token** (`POST api/token/refresh`)
- **Get Student Achievements** (`GET /student/achievements/{student_id}/`)

## Setup and Running the Project

Follow these steps to run the project on your local machine:

### 1. Create a Python Virtual Environment

To isolate the project dependencies, create a virtual environment.

```bash
python3 -m venv venv
```

### 2. Activate Python Virtual Environment and install necessary packages
Activate the virtual environment based on your operating system:
```bash
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Setup PostgreSQL
Login into Postgres and create the required database:
```sql
CREATE DATABASE slate;
```

### 4. Update `slate/settings.py` with your PostgreSQL credentials
Activate the virtual environment based on your operating system:
```javascript
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'slate',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Make Migrations and Migrate
Run the following commands to create the necessary database tables and apply migrations:
```python
python manage.py makemigrations
python manage.py migrate
```

### 6. Run the Django Development Server
Finally, run the Django development server:
```python
python manage.py runserver
```

The server should now be running on http://localhost:8000/.  
Testing can be done using Postman collection included within project directory.