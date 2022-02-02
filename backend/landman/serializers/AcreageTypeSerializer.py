from rest_framework import serializers
from landman.models import AcreageType

class AcreageTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcreageType
        fields = ('code', 'description')