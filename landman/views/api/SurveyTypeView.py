from rest_framework import viewsets
from landman.serializers import SurveyTypeSerializer
from landman.models import SurveyType

class SurveyTypeView(viewsets.ModelViewSet):
    serializer_class = SurveyTypeSerializer
    queryset = SurveyType.objects.all()