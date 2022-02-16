from rest_framework import viewsets
from landman.serializers import TaskStatusSerializer
from landman.models import TaskStatus

class TaskStatusView(viewsets.ModelViewSet):
    serializer_class = TaskStatusSerializer
    queryset = TaskStatus.objects.all()
