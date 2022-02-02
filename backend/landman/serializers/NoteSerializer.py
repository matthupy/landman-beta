from rest_framework import serializers
from landman.models import Note

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('text', 'update_user', 'update_date')