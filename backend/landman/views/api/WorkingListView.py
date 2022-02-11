from rest_framework import viewsets
from landman.serializers import WorkingListSerializer
from landman.models import WorkingList

class WorkingListView(viewsets.ModelViewSet):
    serializer_class = WorkingListSerializer
    queryset = WorkingList.objects.all()