from django import forms

from notes.models import TodoList


class TaskForm(forms.ModelForm):
    """
    Form for creating and editing TodoList tasks
    """

    class Meta:
        model = TodoList
        # The fields should be same as the fields in the database (models.py file)
        fields = ["task", "is_completed"]

        # Add custom widgets for better styling and UX
        widgets = {
            "task": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter your task...",
                    "required": True,
                    "maxlength": 200,
                }
            ),
            "is_completed": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
        }

        # Custom labels
        labels = {
            "task": "Task Description",
            "is_completed": "Mark as completed",
        }

        # Help text for fields
        help_texts = {
            "task": "Enter a brief description of your task (max 200 characters)",
        }

    def clean_task(self):
        """
        Custom validation for task field
        """
        task = self.cleaned_data.get("task")

        # Strip whitespace
        if task:
            task = task.strip()

        # Check if task is empty after stripping
        if not task:
            raise forms.ValidationError(
                "Task cannot be empty or contain only whitespace!"
            )

        # Check minimum length
        if len(task) < 3:
            raise forms.ValidationError("Task must be at least 3 characters long!")

        return task
