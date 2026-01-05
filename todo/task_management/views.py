from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from task_management.models import ToDo
from task_management.forms import ToDoForm

# Create your views here.

class ToDoListView(LoginRequiredMixin,ListView):
    model = ToDo
    template_name = "todo_list.html"
    context_object_name = "todo_list"
    paginate_by = 5
    
    def get_queryset(self):
        context_list = ToDo.objects.filter(created_by=self.request.user)
        return context_list
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['form'] = ToDoForm()
        return context
        
    
    
class ToDoDetailView(LoginRequiredMixin,DetailView):
    model = ToDo
    template_name = "todo_details.html"
    context_object_name = "todo"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ToDoForm()
        return context
    
    def get_queryset(self):
        return ToDo.objects.filter(created_by=self.request.user)
    
    
    
class ToDoCreateView(LoginRequiredMixin,CreateView):
    model = ToDo
    form_class = ToDoForm
    success_url = reverse_lazy("todo_list")
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
    
    def get_initial(self):
        initial = super().get_initial()
        initial['created_by'] = self.request.user
        return initial


class TodoUpdateView(LoginRequiredMixin,UpdateView):
    model = ToDo
    form_class = ToDoForm
    success_url = reverse_lazy('todo_list')
    
    def get_queryset(self):
        return ToDo.objects.filter(created_by=self.request.user)
    
    
    
class TodoDeleteView(LoginRequiredMixin, DeleteView):
    model = ToDo
    success_url = reverse_lazy('todo_list')
        
    
    