from django.shortcuts import render
from django.views import View
from .models import Task
from django.shortcuts import redirect
from .form import TaskForm
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView,UpdateView,DeleteView

class TaskListView(View):
    def get(self, request):
        tasks = Task.objects.all()  
        return render(request, 'tasks/task_list.html', {'tasks': tasks})  

class TaskCreateView(View):
    def get(self, request):
        form = form.TaskForm()
        return render(request, 'tasks/task_form.html', {'form': form})

    def post(self, request):
        form = form.TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
        return render(request, 'tasks/task_form.html', {'form': form})
    
class TaskUpdateView(View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)  # Get the task by primary key
        form = form.TaskForm(instance=task)  # Create a form with the task data
        return render(request, 'tasks/task_form.html', {'form': form})  # Render the form

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)  # Get the task again
        form = form.TaskForm(request.POST, instance=task)  # Load form data
        if form.is_valid():  # Validate the form
            form.save()  # Save changes
            return redirect('task_list')  # Redirect to the task list
        return render(request, 'tasks/task_form.html', {'form': form})  # Display form with errors

class TaskDeleteView(View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)  # Get the task by primary key
        return render(request, 'tasks/task_confirm_delete.html', {'task': task})  # Render the delete confirmation page

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)  # Get the task again
        task.delete()  # Delete the task
        return redirect('task_list')  # Redirect to the task list

class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task_list')

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task_list')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('task_list')

class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'
    paginate_by = 10  # Number of tasks per page

    def get_queryset(self):
        query = self.request.GET.get('search', '')
        return Task.objects.filter(title__icontains=query)

def toggle_task_completion(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')
