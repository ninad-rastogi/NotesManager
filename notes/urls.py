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
    path("", views.homepage, name="home"),
    path("notes", views.notes, name="notes"),
    path("contact", views.contact, name="contact"),
    path("about", views.about, name="about"),
    path("todolist", views.todolist, name="todolist"),
    path("delete_task/<task_id>", views.delete_task, name="delete_task"),
    path("edit_task/<int:task_id>/", views.edit_task, name="edit_task"),
    path("toggle_task/<int:task_id>/", views.toggle_task, name="toggle_task"),
]
