from rest_framework import serializers
from landman.models import Landowner

class LandownerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Landowner
        fields = ('name', 'entity_type', 'address', 'email', 'ssn', 'backupWithholdingType', 'backupWithholding')