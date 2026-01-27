# urls.py

from django.urls import path
from task_management.api_modules.views import taskView

urlpatterns = [
    path('v2/task/', taskView, name='task'),
]
