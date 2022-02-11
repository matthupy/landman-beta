from rest_framework import viewsets
from landman.serializers import CountrySerializer
from landman.models import Country

class CountryView(viewsets.ModelViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()