from rest_framework import serializers
from landman.models import Agreement

class AgreementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agreement
        fields = ('name', 'number', 'type', 'status', 'stage', 'landDivision', 'originalLessee', 'agreementDate', 'effectiveDate', 'term', 'rights', 'related', 'wells')