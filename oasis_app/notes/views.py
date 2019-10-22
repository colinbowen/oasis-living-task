from django.shortcuts import render
from rest_framework import viewsets
from .models import Note, User, LocationLog
from .serializers import NoteSerializer, UserSerializer, LocationSerializer

# Create your views here.
class NoteView(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LocationLogView(viewsets.ModelViewSet):
    queryset = LocationLog.objects.all()
    serializer_class = LocationSerializer