from django.urls import include, path

from notes import views

urlpatterns = [
    # path(
    #     "", views.notes, name="notes"
    # ),  # This is the end point of the app. If I open localhost:8000/tasks/, it will call notes function in views.py file
    # Here "name" parameter is used to give a unique name to this URL pattern so that it can be referenceed elsewhere in Django, such as in template or reverse function. It is just like id in HTML.
    # path("notes/", views.notes, name="notes"),   # This will be the endpoint if I open localhost:8000/tasks/notes/
    # path("http/", views.notes_http, name="notes_http"),
    # path("json/", views.notes_json, name="notes_json"),
    # path("html/", views.notes_html, name="notes_html"),
    # Homepage - displays welcome message
    path("", views.homepage, name="home"),
    # Notes page - displays notes (to be implemented)
    path("notes/", views.notes, name="notes"),
    # Contact page - displays contact information
    path("contact/", views.contact, name="contact"),
    # About page - displays about information
    path("about/", views.about, name="about"),
    # TodoList page - displays all tasks and allows adding new ones
    path("todolist/", views.todolist, name="todolist"),
    # Delete a specific task by ID
    # Example: /delete_task/1 will delete the task with id=1
    path("delete_task/<int:task_id>/", views.delete_task, name="delete_task"),
    # Edit a specific task by ID (AJAX endpoint)
    # Example: /edit_task/1/ will edit the task with id=1
    path("edit_task/<int:task_id>/", views.edit_task, name="edit_task"),
    # Toggle task completion status by ID (AJAX endpoint)
    # Example: /toggle_task/1/ will toggle completion status of task with id=1
    path("toggle_task/<int:task_id>/", views.toggle_task, name="toggle_task"),
]
