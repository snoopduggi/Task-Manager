from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer
from django.http import JsonResponse

def home(request):
    """Basic home view to check if the server is running."""
    return JsonResponse({"message": "Welcome to the Task Manager API!"})


@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_tasks(request):
    """Handles API requests to fetch or create tasks"""

    if request.method == 'GET':  # Fetch tasks only for the logged-in user
        tasks = Task.objects.filter(user=request.user)  # 🔹 Secure: Only user's tasks
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':  # Create new task
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)  # 🔹 Secure: Assign task to user
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def task_detail(request, task_id):
    """Handles API requests to update or delete a task"""

    try:
        task = Task.objects.get(id=task_id, user=request.user)  # 🔹 Secure: Only fetch user's task
    except Task.DoesNotExist:
        return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':  # Update Task
        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':  # Delete Task
        task.delete()
        return Response({"message": "Task deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
