from rest_framework import viewsets
from landman.serializers import AgreementSerializer
from landman.models import Agreement

class AgreementView(viewsets.ModelViewSet):
    serializer_class = AgreementSerializer
    queryset = Agreement.objects.all()