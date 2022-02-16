from rest_framework import viewsets
from landman.serializers import BackupWithholdingTypeSerializer
from landman.models import BackupWithholdingType

class BackupWithholdingTypeView(viewsets.ModelViewSet):
    serializer_class = BackupWithholdingTypeSerializer
    queryset = BackupWithholdingType.objects.all()
