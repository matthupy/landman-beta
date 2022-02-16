from rest_framework import serializers
from landman.models import State

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ('country','code','abbreviation','name','survey','update_date','update_user','hidden')
