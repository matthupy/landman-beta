from rest_framework import serializers
from landman.models import AgreementStatus

class AgreementStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgreementStatus
        fields = ('code', 'description')