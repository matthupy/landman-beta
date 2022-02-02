from rest_framework import serializers
from landman.models import ProjectProgressDate

class ProjectProgressDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectProgressDate
        fields = ('type','status','due_date','completed_date','assigned_to','update_user','update_date')