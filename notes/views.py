import json

from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods

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
    """
    Render the homepage
    """
    context = {"page": "Homepage"}
    return render(request, "homepage.html", context)


def notes(request):
    """
    Render the notes page
    """
    context = {"page": "Notes"}
    return render(request, "notes.html", context)


def contact(request):
    """
    Render the contact page
    """
    context = {"page": "Contact"}
    return render(request, "contact.html", context)


def about(request):
    """
    Render the about page
    """
    context = {"page": "About"}
    return render(request, "about.html", context)


def todolist(request):
    """
    Display all tasks and handle new task creation
    """
    if request.method == "POST":
        # Create a form instance with POST data
        form_data = TaskForm(request.POST or None)

        if form_data.is_valid():
            # Save the new task to database
            form_data.save()
            messages.success(request, "Task added successfully!")
            # Redirect to the same page to see the updated list
            # This prevents form resubmission on page refresh
            return redirect("todolist")
        else:
            messages.error(request, "Something went wrong! Please check your input.")

    # Get all tasks from database, ordered by completion status (incomplete first)
    todolist_content = TodoList.objects.all().order_by("is_completed", "-id")

    context = {"page": "Things To Do", "tasks": todolist_content}
    return render(request, "todolist.html", context)


@require_http_methods(["GET"])
def delete_task(request, task_id):
    """
    Delete a specific task
    Args:
        task_id: The ID of the task to delete
    """
    # Use get_object_or_404 for better error handling
    task_to_delete = get_object_or_404(TodoList, id=task_id)
    task_name = task_to_delete.task
    task_to_delete.delete()
    messages.success(request, f'Task - "{task_name}" deleted successfully!')
    return redirect("todolist")


@require_http_methods(["POST"])
def edit_task(request, task_id):
    """
    Edit a specific task (AJAX endpoint)
    Args:
        task_id: The ID of the task to edit
    Returns:
        JsonResponse with success status and message
    """
    try:
        # Get the task object or return 404
        task = get_object_or_404(TodoList, id=task_id)

        # Parse JSON data from request body
        data = json.loads(request.body)
        new_task_text = data.get("task", "").strip()

        # Validate that task is not empty
        if not new_task_text:
            return JsonResponse(
                {"success": False, "message": "Task cannot be empty!"}, status=400
            )

        # Update the task
        task.task = new_task_text
        task.save()

        messages.success(request, "Task edited successfully!")
        return JsonResponse({"success": True, "message": "Task updated successfully!"})

    except json.JSONDecodeError:
        return JsonResponse(
            {"success": False, "message": "Invalid JSON data!"}, status=400
        )

    except Exception as e:
        return JsonResponse(
            {"success": False, "message": f"An error occurred: {str(e)}"}, status=500
        )


@require_http_methods(["POST"])
def toggle_task(request, task_id):
    """
    Toggle task completion status (AJAX endpoint)
    Args:
        task_id: The ID of the task to toggle
    Returns:
        JsonResponse with success status
    """
    try:
        # Get the task object or return 404
        task = get_object_or_404(TodoList, id=task_id)

        # Parse JSON data from request body
        data = json.loads(request.body)
        is_completed = data.get("is_completed", False)

        # Update the completion status
        task.is_completed = is_completed
        task.save()

        status_text = "completed" if is_completed else "incomplete"

        return JsonResponse(
            {
                "success": True,
                "message": f"Task marked as {status_text} successfully!",
                "is_completed": is_completed,
            }
        )

    except json.JSONDecodeError:
        return JsonResponse(
            {"success": False, "message": "Invalid JSON data!"}, status=400
        )

    except Exception as e:
        return JsonResponse(
            {"success": False, "message": f"An error occurred: {str(e)}"}, status=500
        )
