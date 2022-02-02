from rest_framework import serializers
from landman.models import JeffLegalHeader

class JeffLegalHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = JeffLegalHeader
        fields = ('country','state','county','townshipNum','townshipDir','rangeNum','rangeDir','section')