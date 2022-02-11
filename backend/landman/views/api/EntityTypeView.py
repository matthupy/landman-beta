from rest_framework import viewsets
from landman.serializers import EntityTypeSerializer
from landman.models import EntityType

class EntityTypeView(viewsets.ModelViewSet):
    serializer_class = EntityTypeSerializer
    queryset = EntityType.objects.all()