from django import forms
from task_management.models import (
    Task, User, Category
)

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'title', 'priority', 'description', 'status', 
            'due_date', 'created_by', 'category', 'tags'
        ]
        

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username', 'first_name', 'email', 'password',
        ]
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description', 'created_by']