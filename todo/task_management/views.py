from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from task_management.models import (
    Task, Category, Comment, Attachment, Tag
)
from task_management.forms import (
    TaskForm, CategoryForm
)

# Create your views here.

class TaskListView(LoginRequiredMixin,ListView):
    model = Task
    template_name = "todo_list.html"
    context_object_name = "todo_list"
    paginate_by = 5
    
    def get_queryset(self):
        context_list = Task.objects.filter(created_by=self.request.user).select_related('category').prefetch_related('tags')
        return context_list
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['form'] = TaskForm()
        context['category'] = Category.objects.filter(created_by=self.request.user)
        return context
    
    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")

        if name:
            Category.objects.create(
                name=name,
                created_by=request.user
            )

        return redirect("todo_list")
        
    
    
class TaskDetailView(LoginRequiredMixin,DetailView):
    model = Task
    template_name = "todo_details.html"
    context_object_name = "todo"
    
    def get_queryset(self):
        return Task.objects.filter(created_by=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TaskForm(instance=self.object)
        context['category'] = Category.objects.filter(created_by=self.request.user)
        return context
    
    
    
    
class TaskCreateView(LoginRequiredMixin,CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo_list")
    template_name = "todo_list.html"  
    
    
    def get_initial(self):
        initial = super().get_initial()
        initial['created_by'] = self.request.user
        return initial
    
    def get_form(self, form_class = None):
        form = super().get_form(form_class)
        form.fields['category'].queryset = Category.objects.filter(
            created_by=self.request.user
            )
        form.fields['tags'].queryset = Tag.objects.filter(
            created_by=self.request.user
        )
        return form

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin,UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('todo_list')
    
    def get_queryset(self):
        return Task.objects.filter(created_by=self.request.user)
    
    
    
class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('todo_list')



    
class CommentCreateView(LoginRequiredMixin, View):
    
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk, created_by=request.user)
        text = request.POST.get("comment")
        
        if text:
            Comment.objects.create(
                task=task,
                comment=text,
                commented_by=request.user
            )
        return redirect("todo_details", pk=pk)
    
    

class AttachmentCreateView(LoginRequiredMixin, View):
    
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk, created_by=request.user)
        image = request.FILES.get("image")
        
        if image:
            Attachment.objects.create(
                task=task,
                image=image,
                uploaded_by=request.user                    
            )
        return redirect("todo_details", pk=pk)
    
    
class AttachmentDeleteView(LoginRequiredMixin, View):
    
    def post(self, request, pk):
        attachment = get_object_or_404(Attachment, pk=pk, task__created_by=request.user)
        task_pk = attachment.task.pk
        attachment.delete()
        return redirect("todo_details", pk=task_pk)