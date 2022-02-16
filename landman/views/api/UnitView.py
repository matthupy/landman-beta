from rest_framework import viewsets
from landman.serializers import UnitSerializer
from landman.models import Unit

class UnitView(viewsets.ModelViewSet):
    serializer_class = UnitSerializer
    queryset = Unit.objects.all()