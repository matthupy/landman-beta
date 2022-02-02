from rest_framework import serializers
from landman.models import Country

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'code', 'abbreviation', 'name', 'update_date', 'update_user','hidden')
