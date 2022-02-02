from rest_framework import serializers
from landman.models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('name','type','status','effDateFrom','effDateTo','dueDate')