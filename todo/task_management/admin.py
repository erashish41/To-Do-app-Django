from django.contrib import admin
from task_management.models import (
    Task, SubTask, Category, Tag, Comment, Attachment
)

# Register your models here.

admin.site.register(SubTask)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Attachment)

@admin.register(Task)
class ToDoAdmin(admin.ModelAdmin):
    list_display = ['title', 'priority', 'status', 'due_date']
    list_filter = ['priority', 'status', 'due_date']
    search_fields = ['title', 'priority']