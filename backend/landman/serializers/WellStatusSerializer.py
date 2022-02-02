from rest_framework import serializers
from landman.models import WellStatus

class WellStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = WellStatus
        fields = ('code','description')