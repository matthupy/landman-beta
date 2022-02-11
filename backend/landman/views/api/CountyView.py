from rest_framework import viewsets
from landman.serializers import CountySerializer
from landman.models import County

class CountyView(viewsets.ModelViewSet):
    serializer_class = CountySerializer
    queryset = County.objects.all()
