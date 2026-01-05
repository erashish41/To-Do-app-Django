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
    title = models.CharField(max_length=100, blank=True, null=True)
    priority = models.CharField(max_length=10,choices=PRIORITY, default='medium')
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20,choices=STATUS, blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todos")
    
    def __str__(self):
        return f"{self.title} - {self.priority}"

    

