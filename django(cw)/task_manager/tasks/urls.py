from django.urls import path
from .views import TaskCreateView, TaskListView, TaskUpdateView, TaskDeleteView, toggle_task_completion

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),  # List of tasks
    path('create/', TaskCreateView.as_view(), name='task_create'),  # Create a new task
    path('<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),  # Update an existing task
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),  # Delete a task
    path('<int:pk>/toggle/', toggle_task_completion, name='task_toggle'),  # Toggle completion
]
