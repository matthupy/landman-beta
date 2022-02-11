from rest_framework import viewsets
from landman.serializers import AgreementStatusSerializer
from landman.models import AgreementStatus

class AgreementStatusView(viewsets.ModelViewSet):
    serializer_class = AgreementStatusSerializer
    queryset = AgreementStatus.objects.all()
