from django.db import models
from django.contrib.auth.models import User
from utils.models import BaseMixin

# Create your models here.

STATUS = (
    ('pending', 'Pending'),
    ('in_progress', 'In Progress'),
    ('completed', 'Completed'),
)

PRIORITY = (
    ('low', 'Low'),
    ('medium', 'Medium'),
    ('high', 'High'),
)

class ToDo(BaseMixin):
    title = models.CharField(max_length=100)
    priority = models.CharField(max_length=10,choices=PRIORITY, default='medium')
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20,choices=STATUS,default='pending')
    due_date = models.DateField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todos")
    
    def __str__(self):
        return f"{self.title} - {self.priority}"

    

