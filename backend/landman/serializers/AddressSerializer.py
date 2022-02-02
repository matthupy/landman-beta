from rest_framework import serializers
from landman.models import Address

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('attention_line1', 'attention_line2', 'address_line1', 'address_line2', 'city', 'state', 'zip')