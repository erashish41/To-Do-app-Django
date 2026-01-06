from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from task_management.models import (
    Task, SubTask, Category, Tag, Comment, Attachment
)
from task_management.forms import TaskForm

# Create your views here.

class TaskListView(LoginRequiredMixin,ListView):
    model = Task
    template_name = "todo_list.html"
    context_object_name = "todo_list"
    paginate_by = 5
    
    def get_queryset(self):
        context_list = Task.objects.filter(created_by=self.request.user)
        return context_list
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['form'] = TaskForm()
        return context
        
    
    
class TaskDetailView(LoginRequiredMixin,DetailView):
    model = Task
    template_name = "todo_details.html"
    context_object_name = "todo"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TaskForm()
        return context
    
    def get_queryset(self):
        return Task.objects.filter(created_by=self.request.user)
    
    
    
class TaskCreateView(LoginRequiredMixin,CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo_list")
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
    
    def get_initial(self):
        initial = super().get_initial()
        initial['created_by'] = self.request.user
        return initial


class TaskUpdateView(LoginRequiredMixin,UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('todo_list')
    
    def get_queryset(self):
        return Task.objects.filter(created_by=self.request.user)
    
    
    
class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('todo_list')
        
    
    