// TodoList JavaScript Functions

/**
 * Show toast notification
 * @param {string} message - The message to display
 * @param {string} type - The type of toast (success, error, warning, info)
 */
function showToast(message, type = "info") {
  // Create toast container if it doesn't exist
  let toastContainer = document.querySelector(".toast-container");
  if (!toastContainer) {
    toastContainer = document.createElement("div");
    toastContainer.className = "toast-container";
    document.body.appendChild(toastContainer);
  }

  // Check current number of toasts
  const currentToasts = toastContainer.querySelectorAll(".toast:not(.fade-up)");

  // If we already have 2 toasts, remove the oldest one with fade-up animation
  if (currentToasts.length >= 2) {
    const oldestToast = currentToasts[0];
    oldestToast.classList.add("fade-up");

    // Remove the toast after animation completes
    setTimeout(() => {
      oldestToast.remove();
    }, 400);
  }

  // Map type to Bootstrap classes
  const typeMap = {
    success: "bg-success",
    error: "bg-danger",
    warning: "bg-warning",
    info: "bg-info",
  };

  const iconMap = {
    success: "bi-check-circle-fill",
    error: "bi-exclamation-triangle-fill",
    warning: "bi-exclamation-circle-fill",
    info: "bi-info-circle-fill",
  };

  const bgClass = typeMap[type] || "bg-info";
  const iconClass = iconMap[type] || "bi-info-circle-fill";

  // Create unique ID for this toast
  const toastId = "toast-" + Date.now();

  // Create toast element
  const toastHTML = `
        <div id="${toastId}" class="toast ${bgClass}" role="alert" aria-live="assertive" aria-atomic="true">
            <div class="toast-header">
                <i class="bi ${iconClass} me-2"></i>
                <strong class="me-auto">Notification</strong>
                <button type="button" class="btn-close btn-close-white" data-bs-dismiss="toast" aria-label="Close"></button>
            </div>
            <div class="toast-body">
                ${message}
            </div>
        </div>
    `;

  // Add toast to container
  toastContainer.insertAdjacentHTML("beforeend", toastHTML);

  // Initialize and show toast
  const toastElement = document.getElementById(toastId);
  const toast = new bootstrap.Toast(toastElement, {
    autohide: true,
    delay: 5000, // 5 seconds
  });

  toast.show();

  // Remove toast element from DOM after it's hidden
  toastElement.addEventListener("hidden.bs.toast", function () {
    toastElement.remove();
  });
}

/**
 * Process Django messages and show as toasts
 */
document.addEventListener("DOMContentLoaded", function () {
  // Get all Django messages
  const messages = document.querySelectorAll('.alert[role="alert"]');

  messages.forEach(function (alertElement) {
    const message = alertElement.textContent.trim();
    let type = "info";

    // Determine toast type from alert classes
    if (alertElement.classList.contains("alert-success")) {
      type = "success";
    } else if (alertElement.classList.contains("alert-danger")) {
      type = "error";
    } else if (alertElement.classList.contains("alert-warning")) {
      type = "warning";
    }

    // Show toast
    showToast(message, type);

    // Remove the alert element
    alertElement.remove();
  });
});

/**
 * Enable edit mode for a task
 * @param {number} taskId - The ID of the task to edit
 */
function enableEdit(taskId) {
  // Hide the task text and show the input field
  document.getElementById(`task-text-${taskId}`).style.display = "none";
  document.getElementById(`task-input-${taskId}`).style.display = "block";

  // Hide edit button and show save/cancel buttons
  document.getElementById(`edit-btn-${taskId}`).style.display = "none";
  document.getElementById(`save-btn-${taskId}`).style.display = "inline-block";
  document.getElementById(`cancel-btn-${taskId}`).style.display =
    "inline-block";

  // Focus on the input field
  document.getElementById(`task-input-${taskId}`).focus();
}

/**
 * Cancel edit mode for a task
 * @param {number} taskId - The ID of the task to cancel editing
 */
function cancelEdit(taskId) {
  // Show the task text and hide the input field
  document.getElementById(`task-text-${taskId}`).style.display = "inline";
  document.getElementById(`task-input-${taskId}`).style.display = "none";

  // Show edit button and hide save/cancel buttons
  document.getElementById(`edit-btn-${taskId}`).style.display = "inline-block";
  document.getElementById(`save-btn-${taskId}`).style.display = "none";
  document.getElementById(`cancel-btn-${taskId}`).style.display = "none";

  // Reset input value to original
  const originalText = document.getElementById(
    `task-text-${taskId}`
  ).textContent;
  document.getElementById(`task-input-${taskId}`).value = originalText;
}

/**
 * Save edited task
 * @param {number} taskId - The ID of the task to save
 */
function saveEdit(taskId) {
  const newTaskText = document.getElementById(`task-input-${taskId}`).value;

  // Validate that task is not empty
  if (newTaskText.trim() === "") {
    showToast("Task cannot be empty!", "error");
    return;
  }

  // Send AJAX request to update the task
  fetch(`/edit_task/${taskId}/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": getCookie("csrftoken"),
    },
    body: JSON.stringify({
      task: newTaskText,
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.success) {
        // Update the task text in the DOM
        document.getElementById(`task-text-${taskId}`).innerText = newTaskText;
        cancelEdit(taskId);
        // Show success toast
        showToast("Task updated successfully!", "success");
      } else {
        showToast("Error updating task: " + data.message, "error");
      }
    })
    .catch((error) => {
      console.error("Error:", error);
      showToast("An error occurred while updating the task.", "error");
    });
}

/**
 * Toggle task completion status
 * @param {number} taskId - The ID of the task to toggle
 * @param {HTMLElement} checkbox - The checkbox element
 */
function toggleTask(taskId, checkbox) {
  const isCompleted = checkbox.checked;

  // Send AJAX request to update the task completion status
  fetch(`/toggle_task/${taskId}/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": getCookie("csrftoken"),
    },
    body: JSON.stringify({
      is_completed: isCompleted,
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.success) {
        // Update the row styling
        const row = checkbox.closest("tr");
        const taskText = document.getElementById(`task-text-${taskId}`);
        const statusBadge = row.querySelector(".status-badge");

        if (isCompleted) {
          row.classList.remove("table-danger");
          row.classList.add("table-success");
          taskText.classList.add("task-completed");
          statusBadge.classList.remove("bg-danger");
          statusBadge.classList.add("bg-success");
          statusBadge.textContent = "Completed";
          showToast("Task marked as completed!", "success");
        } else {
          row.classList.remove("table-success");
          row.classList.add("table-danger");
          taskText.classList.remove("task-completed");
          statusBadge.classList.remove("bg-success");
          statusBadge.classList.add("bg-danger");
          statusBadge.textContent = "Not Completed";
          showToast("Task marked as incomplete!", "info");
        }
      } else {
        // Revert checkbox if update failed
        checkbox.checked = !isCompleted;
        showToast("Error updating task status: " + data.message, "error");
      }
    })
    .catch((error) => {
      console.error("Error:", error);
      // Revert checkbox if request failed
      checkbox.checked = !isCompleted;
      showToast("An error occurred while updating the task.", "error");
    });
}

/**
 * Confirm and delete task
 * @param {string} url - The delete URL
 * @param {string} taskName - The name of the task to delete
 * @returns {boolean} - Return false to prevent default link behavior
 */
function confirmDelete(url, taskName) {
  if (confirm(`Are you sure you want to delete the task: "${taskName}"?`)) {
    window.location.href = url;
  }
  return false;
}

/**
 * Get CSRF token from cookies
 * @param {string} name - The name of the cookie
 * @returns {string|null} - The cookie value or null if not found
 */
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Check if this cookie string begins with the name we want
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
