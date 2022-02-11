from rest_framework import viewsets
from landman.serializers import TaskSerializer
from landman.models import Task

class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()