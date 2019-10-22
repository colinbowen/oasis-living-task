from django.shortcuts import render
from rest_framework import viewsets
from .models import Note, LocationLog
from .serializers import NoteSerializer, LocationSerializer

# Create your views here.
class NoteView(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class LocationLogView(viewsets.ModelViewSet):
    queryset = LocationLog.objects.all()
    serializer_class = LocationSerializer