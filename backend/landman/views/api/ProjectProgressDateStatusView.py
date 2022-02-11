from rest_framework import viewsets
from landman.serializers import ProjectProgressDateStatusSerializer
from landman.models import ProjectProgressDateStatus

class ProjectProgressDateStatusView(viewsets.ModelViewSet):
    serializer_class = ProjectProgressDateStatusSerializer
    queryset = ProjectProgressDateStatus.objects.all()