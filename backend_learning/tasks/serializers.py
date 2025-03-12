from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task  # Connects serializer to Task model
        fields = '__all__'  # Includes all fields