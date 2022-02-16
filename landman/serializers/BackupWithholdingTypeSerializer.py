from rest_framework import serializers
from landman.models import BackupWithholdingType

class BackupWithholdingTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackupWithholdingType
        fields = ('code', 'description')