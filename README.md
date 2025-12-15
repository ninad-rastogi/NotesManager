# NotesManager - Django Todo List Application

A simple and elegant Notes Manager application built with Django and Bootstrap 5. This application allows users to create, edit, delete, and manage their daily tasks efficiently.

## Features

- ✅ Create new tasks
- ✏️ Edit existing tasks inline
- 🗑️ Delete tasks with confirmation
- ✔️ Mark tasks as completed/incomplete
- 📱 Responsive design with Bootstrap 5
- 🎨 Clean and modern UI with Bootstrap Icons
- 🔔 Real-time notifications for user actions
- 📊 Visual status indicators (color-coded rows)

## Project Structure

```
NotesManager/
├── NotesManager/           # Main project directory
│   ├── __init__.py
│   ├── settings.py        # Project settings
│   ├── urls.py            # Main URL configuration
│   ├── wsgi.py
│   └── asgi.py
├── notes/                  # Notes app directory
│   ├── migrations/        # Database migrations
│   ├── templates/         # App-specific templates
│   │   ├── about.html
│   │   ├── contact.html
│   │   ├── homepage.html
│   │   ├── notes.html
│   │   └── todolist.html
│   ├── __init__.py
│   ├── admin.py           # Admin configuration
│   ├── apps.py
│   ├── forms.py           # Form definitions
│   ├── models.py          # Database models
│   ├── tests.py
│   ├── urls.py            # App URL configuration
│   └── views.py           # View functions
├── templates/             # Global templates
│   └── base.html          # Base template
├── static/                # Static files
│   ├── css/
│   │   └── todolist.css   # Custom CSS
│   ├── js/
│   │   └── todolist.js    # Custom JavaScript
│   └── image/
│       └── notes.png      # Logo
├── manage.py              # Django management script
└── README.md              # This file
```

## Technologies Used

- **Backend**: Django 5.2.9
- **Frontend**: Bootstrap 5.3.8, Bootstrap Icons 1.11.3
- **Database**: MySQL (can be changed to PostgreSQL or SQLite)
- **JavaScript**: Vanilla JS (no framework dependencies)

## Installation

### Prerequisites

- Python 3.8 or higher
- MySQL Server (or any other database of your choice)
- pip (Python package manager)

### Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/ninad-rastogi/NotesManager.git
   ```

2. **Create and activate virtual environment** (recommended)

   ```bash
   python -m venv venv

   # On Windows
   venv\Scripts\activate

   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install django mysqlclient
   ```

4. **Configure database**

   - Open `NotesManager/settings.py`
   - Update the `DATABASES` configuration with your MySQL credentials:

   ```python
   DATABASES = {
       "default": {
           "ENGINE": "django.db.backends.mysql",
           "NAME": "notesmanager",
           "USER": "your_mysql_username",
           "PASSWORD": "your_mysql_password",
           "HOST": "localhost",
           "PORT": "3306",
       }
   }
   ```

5. **Create database**

   ```bash
   # Login to MySQL
   mysql -u root -p

   # Create database
   CREATE DATABASE notesmanager;

   # Exit MySQL
   exit;
   ```

6. **Run migrations**

   ```bash
   # Create new migrations (due to model changes)
   python manage.py makemigrations

   # Apply migrations to database
   python manage.py migrate
   ```

7. **Create superuser** (optional, for admin access)

   ```bash
   python manage.py createsuperuser
   ```

8. **Collect static files** (for production)

   ```bash
   python manage.py collectstatic
   ```

9. **Run development server**

   ```bash
   python manage.py runserver
   ```

10. **Access the application**
    - Main application: http://localhost:8000/
    - Admin panel: http://localhost:8000/admin/

## Recent Changes and Improvements

### 1. Separated JavaScript and CSS

- Moved all inline JavaScript from `todolist.html` to `static/js/todolist.js`
- Created custom CSS file at `static/css/todolist.css`
- Improved code organization and maintainability

### 2. Bootstrap Icons Integration

- Replaced SVG icons with Bootstrap Icons
- Added icon CDN to `base.html`
- Improved visual consistency across the application

### 3. Enhanced Models

- Added `created_at` and `updated_at` timestamp fields
- Added custom model methods (`mark_as_completed`, `mark_as_incomplete`)
- Improved model metadata and ordering

### 4. Improved Views

- Added proper error handling with try-except blocks
- Used `get_object_or_404` for better 404 error handling
- Added `@require_http_methods` decorators for better security
- Fixed `edit_task` function to return proper JsonResponse
- Added input validation

### 5. Enhanced Forms

- Added custom form validation
- Added Bootstrap classes to form widgets
- Added help text and custom labels
- Improved user feedback

### 6. Better Admin Interface

- Added custom admin class with list filters
- Added search functionality
- Added bulk actions (mark as completed/incomplete)
- Added date hierarchy navigation
- Organized fields in fieldsets

### 7. Improved URL Configuration

- Added detailed comments
- Changed trailing slashes for consistency
- Better organization and readability

### 8. Enhanced UI/UX

- Added confirmation dialog for delete action
- Improved navigation with active link highlighting
- Added icons to navigation menu
- Better responsive design
- Added empty state message when no tasks exist

## Usage

### Adding a Task

1. Navigate to the "ToDo List" page
2. Enter your task in the input field
3. Click "Add Task" button
4. Task will be added to the list with "Not Completed" status

### Editing a Task

1. Click the pencil icon (Edit) next to the task
2. Modify the task text inline
3. Click the check icon (Save) to save changes
4. Or click the X icon (Cancel) to discard changes

### Deleting a Task

1. Click the trash icon (Delete) next to the task
2. Confirm the deletion in the popup dialog
3. Task will be permanently removed

### Task Status

- Tasks are color-coded:
  - **Red** (table-danger): Not completed tasks
  - **Green** (table-success): Completed tasks

## Database Migrations

Since the models have been updated with new fields (`created_at` and `updated_at`), you need to create and apply new migrations:

```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate
```

## Configuration Options

### Changing Database

To use SQLite instead of MySQL, update `settings.py`:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
```

### Debug Mode

For production, set `DEBUG = False` in `settings.py` and add your domain to `ALLOWED_HOSTS`:

```python
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
```

## API Endpoints

### GET Endpoints

- `/` - Homepage
- `/todolist/` - View all tasks
- `/notes/` - Notes page
- `/contact/` - Contact page
- `/about/` - About page
- `/delete_task/<task_id>/` - Delete a task

### POST Endpoints (AJAX)

- `/edit_task/<task_id>/` - Edit a task
- `/toggle_task/<task_id>/` - Toggle task completion status

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request

## Future Enhancements

- [ ] Add user authentication and authorization
- [ ] Add task categories/tags
- [ ] Add due dates and reminders
- [ ] Add task priority levels
- [ ] Add search and filter functionality
- [ ] Add task sorting options
- [ ] Add data export functionality (CSV, PDF)
- [ ] Add REST API for mobile app integration
- [ ] Add task sharing functionality
- [ ] Add dark mode toggle

## Troubleshooting

### Common Issues

**Issue**: Migration errors

```bash
# Solution: Reset migrations and database
python manage.py migrate --run-syncdb
```

**Issue**: Static files not loading

```bash
# Solution: Collect static files
python manage.py collectstatic --noinput
```

**Issue**: MySQL connection error

```bash
# Solution: Check MySQL service is running and credentials are correct
# Ensure mysqlclient is installed: pip install mysqlclient
```

## License

This project is open source and available under the MIT License.

## Contact

For any queries or suggestions, please visit the Contact Us page in the application.

## Acknowledgments

- Django Documentation
- Bootstrap Documentation
- Bootstrap Icons
- Python Community

---

**Note**: This is a learning project created for educational purposes.
