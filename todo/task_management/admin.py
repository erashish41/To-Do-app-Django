from django.contrib import admin
from task_management.models import ToDo

# Register your models here.

@admin.register(ToDo)
class ToDoAdmin(admin.ModelAdmin):
    list_display = ['title', 'priority', 'status', 'due_date']
    list_filter = ['priority', 'status', 'due_date']
    search_fields = ['title', 'priority']