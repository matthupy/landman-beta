from django.shortcuts import render
from rest_framework import viewsets
from landman.serializers import AcreageSerializer
from landman.models import Acreage

class AcreageView(viewsets.ModelViewSet):
    serializer_class = AcreageSerializer
    queryset = Acreage.objects.all()