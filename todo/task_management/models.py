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


class Category(BaseMixin):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="categories")
    
    def __str__(self):
        return f"{self.name} - {self.created_by}"
    
    
class Tag(BaseMixin):
    name = models.CharField(max_length=30, unique=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tags")

    def __str__(self):
        return f"{self.name} - {self.created_by}"


class SubTask(BaseMixin):
    task = models.ForeignKey("Task", on_delete=models.CASCADE, related_name="subtasks")
    title = models.CharField(max_length=100)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
class Task(BaseMixin):
    title = models.CharField(max_length=100)
    priority = models.CharField(max_length=10,choices=PRIORITY, default='medium')
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20,choices=STATUS,default='pending')
    due_date = models.DateField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todos")
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="category")
    tags = models.ManyToManyField("Tag", blank=True)

    
    def __str__(self):
        return f"{self.title} - {self.priority}"

    
class Comment(BaseMixin):
    task = models.ForeignKey("Task", on_delete=models.CASCADE, related_name="comments")
    comment = models.TextField()
    commented_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.todo.title}"
    

class Attachment(BaseMixin):
    task = models.ForeignKey("Task", on_delete=models.CASCADE, related_name="attachments")
    image = models.ImageField(upload_to="todo_images/",blank=True, null=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.task.title}"



    
    
    

    

