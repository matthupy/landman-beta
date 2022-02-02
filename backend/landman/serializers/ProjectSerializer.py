from rest_framework import serializers
from landman.models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('name','number','description','type','status','stage','country','state','county','tasks','contacts','cross_refferences','progress_dates')