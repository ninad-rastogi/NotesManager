from django import forms

from notes.models import TodoList


class TaskForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = [
            "task",
            "is_completed",
        ]  # The fields should be same as the fields in the database (models.py file)
