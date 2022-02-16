from rest_framework import viewsets
from landman.serializers import AgreementStageSerializer
from landman.models import AgreementStage

class AgreementStageView(viewsets.ModelViewSet):
    serializer_class = AgreementStageSerializer
    queryset = AgreementStage.objects.all()