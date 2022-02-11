from rest_framework import viewsets
from landman.serializers import AddressSerializer
from landman.models import Address

class AddressView(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()