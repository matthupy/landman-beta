from rest_framework import serializers
from landman.models import TaskStatus

class TaskStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskStatus
        fields = ('code','description')