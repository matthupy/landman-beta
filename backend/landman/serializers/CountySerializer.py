from rest_framework import serializers
from landman.models import County

class CountySerializer(serializers.ModelSerializer):
    class Meta:
        model = County
        fields = ('id', 'state', 'code', 'name', 'update_date', 'update_user','hidden')