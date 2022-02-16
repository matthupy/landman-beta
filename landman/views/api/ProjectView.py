from rest_framework import viewsets
from landman.serializers import ProjectSerializer
from landman.models import Project

class ProjectView(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
