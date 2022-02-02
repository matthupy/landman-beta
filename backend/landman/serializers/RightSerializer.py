from rest_framework import serializers
from landman.models import Right

class RightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Right
        fields = ('code','description')