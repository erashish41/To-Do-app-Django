from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from task_management.api_modules.serializers import TaskSerializer
from task_management.models import (
    Task, Category, Comment, Attachment, Tag
)


@api_view(["GET"])
def taskView(request):
    if request.method == "GET":
        task = Task.objects.all()
        serializer = TaskSerializer(task, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)