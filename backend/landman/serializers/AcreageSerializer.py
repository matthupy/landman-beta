from rest_framework import serializers
from landman.models import Acreage

class AcreageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acreage
        fields = ('type', 'amount', 'unit', 'agreement')