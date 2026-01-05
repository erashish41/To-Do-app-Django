from django import forms
from task_management.models import ToDo

class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = [
            'title', 'priority', 'description', 'status', 'due_date', 'created_by'
        ]