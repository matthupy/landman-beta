from rest_framework import viewsets
from landman.serializers import LandDivisionSerializer
from landman.models import LandDivision

class LandDivisionView(viewsets.ModelViewSet):
    serializer_class = LandDivisionSerializer
    queryset = LandDivision.objects.all()