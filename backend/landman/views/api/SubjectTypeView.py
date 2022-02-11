from rest_framework import viewsets
from landman.serializers import SubjectTypeSerializer
from landman.models import SubjectType

class SubjectTypeView(viewsets.ModelViewSet):
    serializer_class = SubjectTypeSerializer
    queryset = SubjectType.objects.all()