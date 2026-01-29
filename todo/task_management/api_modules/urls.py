# urls.py

from django.urls import path
from task_management.api_modules.views import (
    taskView, taskDetail, CategoryView, CategoryDetail,
    TagView, TagDetail
    )

urlpatterns = [
    path('v2/task/', taskView, name='task_list'),
    path('v2/task/<uuid:pk>/', taskDetail, name='task_detail'),
    
    path('v2/category/', CategoryView.as_view(), name='category_list'),
    path('v2/category/<uuid:pk>/', CategoryDetail.as_view(), name='category_detail'),
    
    path('v2/tag/', TagView.as_view(), name='tag_list'),
    path('v2/tag/<uuid:pk>/', TagDetail.as_view(), name='tag_detail')
]
