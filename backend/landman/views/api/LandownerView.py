from rest_framework import viewsets
from landman.serializers import LandownerSerializer
from landman.models import Landowner

class LandownerView(viewsets.ModelViewSet):
    serializer_class = LandownerSerializer
    queryset = Landowner.objects.all()