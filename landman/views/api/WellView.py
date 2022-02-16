from rest_framework import viewsets
from landman.serializers import WellSerializer
from landman.models import Well

class WellView(viewsets.ModelViewSet):
    serializer_class = WellSerializer
    queryset = Well.objects.all()