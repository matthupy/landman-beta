from rest_framework import serializers
from landman.models import AgreementType

class AgreementTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgreementType
        fields = ('code', 'category', 'description')