from django.shortcuts import render
from rest_framework import viewsets
from .models import Note, LocationLog
from .serializers import NoteSerializer, LocationSerializer, UserSerializer
from django.contrib.auth.models import User

# Create your views here.

# ViewSets define the view behavior.
class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class NoteView(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class LocationLogView(viewsets.ModelViewSet):
    queryset = LocationLog.objects.all()
    serializer_class = LocationSerializer