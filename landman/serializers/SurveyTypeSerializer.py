from rest_framework import serializers
from landman.models import SurveyType

class SurveyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyType
        fields = ('code','description')