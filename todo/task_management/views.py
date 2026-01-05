from django.shortcuts import render
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from task_management.models import ToDo

# Create your views here.

class ToDoListView(ListView):
    model = ToDo
    template_name = "todo_list.html"
    context_object_name = "todo_list"
    paginate_by = 5
    
    def get_queryset(self):
        context_list = ToDo.objects.filter(created_by=self.request.user)
        return context_list
    
    
class ToDoDetailView(DetailView):
    model = ToDo
    template_name = "todo_details.html"
    context_object_name = "todo_details"