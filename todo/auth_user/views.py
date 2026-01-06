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
    
    
class UserLoginView(LoginView):
    template_name = "auth_user/login_in.html"
    success_url = reverse_lazy("todo_list")
    
    
class UserLogoutView(LogoutView):
    success_url = reverse_lazy("signin")