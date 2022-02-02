from rest_framework import serializers
from landman.models import AgreementStage

class AgreementStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgreementStage
        fields = ('code', 'description', 'index')