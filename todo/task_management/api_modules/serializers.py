from rest_framework import serializers
from task_management.models import (
    Task, Category, Comment, Attachment, Tag
)


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"