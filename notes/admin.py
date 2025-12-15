from django.contrib import admin

from notes.models import TodoList


@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    """
    Admin interface customization for TodoList model
    """

    # Fields to display in the list view
    list_display = ("task", "is_completed", "created_at", "updated_at")

    # Fields that can be clicked to open the detail view
    list_display_links = ("task",)

    # Add filters in the right sidebar
    list_filter = ("is_completed", "created_at", "updated_at")

    # Add search functionality
    search_fields = ("task",)

    # Fields that can be edited directly in the list view
    list_editable = ("is_completed",)

    # Number of items to show per page
    list_per_page = 25

    # Read-only fields in the detail view
    readonly_fields = ("created_at", "updated_at")

    # Organize fields in the detail view
    fieldsets = (
        ("Task Information", {"fields": ("task", "is_completed")}),
        (
            "Timestamps",
            {
                "fields": ("created_at", "updated_at"),
                "classes": ("collapse",),  # Make this section collapsible
            },
        ),
    )

    # Default ordering in admin
    ordering = ("-created_at",)

    # Removed date_hierarchy to avoid MySQL timezone issues
    # date_hierarchy = 'created_at'

    # Actions that can be performed on multiple items
    actions = ["mark_as_completed", "mark_as_incomplete"]

    def mark_as_completed(self, request, queryset):
        """
        Action to mark selected tasks as completed
        """
        updated = queryset.update(is_completed=True)
        self.message_user(request, f"{updated} task(s) marked as completed.")

    mark_as_completed.short_description = "Mark selected tasks as completed"

    def mark_as_incomplete(self, request, queryset):
        """
        Action to mark selected tasks as incomplete
        """
        updated = queryset.update(is_completed=False)
        self.message_user(request, f"{updated} task(s) marked as incomplete.")

    mark_as_incomplete.short_description = "Mark selected tasks as incomplete"
