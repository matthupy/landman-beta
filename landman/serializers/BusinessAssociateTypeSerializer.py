from rest_framework import serializers
from landman.models import BusinessAssociateType

class BusinessAssociateTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessAssociateType
        fields = ('code', 'description')