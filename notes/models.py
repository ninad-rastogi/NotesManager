from django.db import models
from django.utils import timezone


class TodoList(models.Model):
    """
    Model to represent a task in the todo list
    """

    task = models.CharField(
        max_length=200,
        verbose_name="Task Description",
        help_text="Enter the task description (max 200 characters)",
    )
    is_completed = models.BooleanField(
        default=False,
        verbose_name="Completed",
        help_text="Check if the task is completed",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At",
        help_text="Timestamp when the task was created",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Updated At",
        help_text="Timestamp when the task was last updated",
    )

    class Meta:
        verbose_name = "Todo Item"
        verbose_name_plural = "Todo Items"
        ordering = ["-created_at"]  # Order by newest first

    def __str__(self):
        """
        String representation of the TodoList object
        """
        status = "✓" if self.is_completed else "✗"
        return f"{status} {self.task}"

    def mark_as_completed(self):
        """
        Mark the task as completed
        """
        self.is_completed = True
        self.save()

    def mark_as_incomplete(self):
        """
        Mark the task as incomplete
        """
        self.is_completed = False
        self.save()
