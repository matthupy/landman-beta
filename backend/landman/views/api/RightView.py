from rest_framework import viewsets
from landman.serializers import RightSerializer
from landman.models import Right

class RightView(viewsets.ModelViewSet):
    serializer_class = RightSerializer
    queryset = Right.objects.all()
