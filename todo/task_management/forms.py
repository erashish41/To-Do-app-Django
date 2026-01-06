from django import forms
from task_management.models import (
    Task, SubTask, Category, Tag, Comment, Attachment
)

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'title', 'priority', 'description', 'status', 'due_date', 'created_by'
        ]