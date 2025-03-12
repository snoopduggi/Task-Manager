from django.urls import path
from tasks.views import get_tasks, task_detail

urlpatterns = [
    path('tasks/', get_tasks, name='api_get_tasks'),
    path('tasks/<int:task_id>/', task_detail, name='api_task_detail'),
]
