from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from task_management.forms import UserForm
from django.urls import reverse_lazy

# Create your views here.

class UserRegisterView(CreateView):
    form_class = UserForm
    template_name = "auth_user/sign_in.html"
    success_url = reverse_lazy("login")
    
    def form_valid(self, form):
        return super().form_valid(form)
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    
class UserLoginView(LoginView):
    template_name = "auth_user/login_in.html"
    
    def get_success_url(self):
        return reverse_lazy("todo_list")
    
    
class UserLogoutView(LogoutView):
    next_page = reverse_lazy("todo_list")