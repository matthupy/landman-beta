from rest_framework import viewsets
from landman.serializers import ProjectProgressDateSerializer
from landman.models import ProjectProgressDate

class ProjectProgressDateView(viewsets.ModelViewSet):
    serializer_class = ProjectProgressDateSerializer
    queryset = ProjectProgressDate.objects.all()