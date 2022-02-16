from rest_framework import serializers
from landman.models import SubjectType
class SubjectTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectType
        fields = ('code', 'description')