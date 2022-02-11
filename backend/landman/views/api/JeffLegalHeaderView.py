from rest_framework import viewsets
from landman.serializers import JeffLegalHeaderSerializer
from landman.models import JeffLegalHeader

class JeffLegalHeaderView(viewsets.ModelViewSet):
    serializer_class = JeffLegalHeaderSerializer
    queryset = JeffLegalHeader.objects.all()