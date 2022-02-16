from rest_framework import viewsets
from landman.serializers import AgreementTypeSerializer
from landman.models import AgreementType

class AgreementTypeView(viewsets.ModelViewSet):
    serializer_class = AgreementTypeSerializer
    queryset = AgreementType.objects.all()