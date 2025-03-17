
from django.urls import path
from .views import home, get_tasks, task_detail  # Import all necessary views

urlpatterns = [
    path('', home, name='home'),  # Root homepage
    path('all/', get_tasks, name='api_get_tasks'),  # Updated path for getting tasks
    path('<int:task_id>/', task_detail, name='api_task_detail'),  # For specific task
]

