from django.urls import reverse
from django.test import TestCase
from .models import Task
from datetime import date

class TaskModelTest(TestCase):
    def test_string_representation(self):
        task = Task(title="Test Task")
        self.assertEqual(str(task), task.title)

    def test_task_due_date(self):
        task = Task(title="Task with Due Date", due_date=date.today())
        self.assertEqual(task.due_date, date.today())

class TaskViewTests(TestCase):
    def setUp(self):
        self.task = Task.objects.create(
            title="Test Task",
            description="Test Description",
            due_date=date.today(),
            completed=False
        )

    def test_task_list_view(self):
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.task.title)

    def test_task_create_view(self):
        response = self.client.post(reverse('task_create'), {
            'title': 'New Task',
            'description': 'New Description',
            'due_date': date.today(),
            'completed': False
        })
        self.assertEqual(response.status_code, 302)  # Redirects after success
        self.assertEqual(Task.objects.count(), 2)  # Ensure task count increased

    def test_task_delete_view(self):
        response = self.client.post(reverse('task_delete', args=[self.task.id]))
        self.assertEqual(response.status_code, 302)  # Redirects after delete
        self.assertEqual(Task.objects.count(), 0)  # Ensure task is deleted
