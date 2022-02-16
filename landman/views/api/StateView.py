from rest_framework import viewsets
from landman.serializers import StateSerializer
from landman.models import State

class StateView(viewsets.ModelViewSet):
    serializer_class = StateSerializer
    queryset = State.objects.all()