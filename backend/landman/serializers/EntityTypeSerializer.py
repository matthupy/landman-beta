from rest_framework import serializers
from landman.models import EntityType

class EntityTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntityType
        fields = ('code', 'description')