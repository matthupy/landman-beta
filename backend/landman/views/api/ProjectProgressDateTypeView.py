from rest_framework import viewsets
from landman.serializers import ProjectProgressDateTypeSerializer
from landman.models import ProjectProgressDateType

class ProjectProgressDateTypeView(viewsets.ModelViewSet):
    serializer_class = ProjectProgressDateTypeSerializer
    queryset = ProjectProgressDateType.objects.all()