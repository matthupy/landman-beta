from rest_framework import viewsets
from landman.serializers import WellStatusSerializer
from landman.models import WellStatus

class WellStatusView(viewsets.ModelViewSet):
    serializer_class = WellStatusSerializer
    queryset = WellStatus.objects.all()