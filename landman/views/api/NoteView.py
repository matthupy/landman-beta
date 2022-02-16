from rest_framework import viewsets
from landman.serializers import NoteSerializer
from landman.models import Note

class NoteView(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
