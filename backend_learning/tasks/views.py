from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer

# ✅ Web View for Home Page
def home(request):
    """Renders the web-based home page."""
    return render(request, 'tasks/home.html')  # Ensure home.html exists in templates folder

# ✅ API View to List & Create Tasks
@api_view(['GET', 'POST'])
def get_tasks(request):
    """Handles API requests to fetch or create tasks"""

    if request.method == 'GET':  # List all tasks
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':  # Add a new task
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ✅ API View to Update & Delete a Specific Task
@api_view(['PUT', 'DELETE'])
def task_detail(request, task_id):
    """Handles API requests to update or delete a task"""
    
    try:
        task = Task.objects.get(id=task_id)  # Fetch task by ID
    except Task.DoesNotExist:
        return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':  # Update Task
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':  # Delete Task
        task.delete()
        return Response({"message": "Task deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
