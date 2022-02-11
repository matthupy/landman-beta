from rest_framework import viewsets
from landman.serializers import BusinessAssociateTypeSerializer
from landman.models import BusinessAssociateType

class BusinessAssociateTypeView(viewsets.ModelViewSet):
    serializer_class = BusinessAssociateTypeSerializer
    queryset = BusinessAssociateType.objects.all()
