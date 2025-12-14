import json

from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render

from notes.forms import TaskForm
from notes.models import TodoList

# Create your views here.
# This function will be called in the app's urls.py file
# def notes(request):
#     return HttpResponse("<h1>This is the Notes view.</h1>")


# def notes_http(request):
#     return HttpResponse("<h1>This is the Notes view.</h1>")


# def notes_json(requests):
#     data = {"name": "Ninad Rastogi", "age": 27, "location": "Indore"}
#     return JsonResponse(data)


# def notes_html(request):
#     return render(
#         request, "main.html", {}
#     )  # Here {} is the context dictionary to pass the data into the HTML file.


def homepage(request):
    context = {"page": "Homepage"}
    return render(request, "homepage.html", context)


def notes(request):
    context = {"page": "Notes"}
    return render(request, "notes.html", context)


def contact(request):
    context = {"page": "Contact"}
    return render(request, "contact.html", context)


def about(request):
    context = {"page": "About"}
    return render(request, "about.html", context)


def todolist(request):
    if request.method == "POST":
        form_data = TaskForm(request.POST or None)

        if form_data.is_valid():
            form_data.save()
            messages.success(request, "Task added successfully!")
            return redirect(
                "todolist"
            )  # Redirected to the same page to see the updated list. Can be redirected to any other page as well. Just provide the name of the page here and check the urls.py file for the name of the page (endpoint).

        else:
            messages.error(request, "Something went wrong!")

    todolist_content = TodoList.objects.all()

    context = {"page": "Things To Do", "tasks": todolist_content}
    return render(request, "todolist.html", context)


def delete_task(request, task_id):
    task_to_delete = TodoList.objects.get(id=task_id)
    task_to_delete.delete()
    messages.success(request, f'Task - "{task_to_delete.task}" deletd successfully!')
    return redirect("todolist")


def edit_task(request, task_id):
    if request.method == "POST":
        task = TodoList.objects.get(id=task_id)
        data = json.loads(request.body)
        task.task = data.get("task")
        task.save()
        messages.success(request, "Task edited successfully!")


def toggle_task(request, task_id):
    if request.method == "POST":
        data = json.loads(request.body)
        task = TodoList.objects.get(id=task_id)
        task.is_completed = data["is_completed"]
        task.save()
        return JsonResponse({"success": True})
