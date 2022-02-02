from rest_framework import serializers
from landman.models import ProjectProgressDateStatus

class ProjectProgressDateStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectProgressDateStatus
        fields = ('code','description')