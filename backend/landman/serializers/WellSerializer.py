from rest_framework import serializers
from landman.models import Well

class WellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Well
        fields = ('name','status','latitude','longitude')