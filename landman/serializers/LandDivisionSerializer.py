from rest_framework import serializers
from landman.models import LandDivision

class LandDivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandDivision
        fields = ('code','description')