from rest_framework import serializers
from .models import Note, LocationLog
from django.contrib.auth.models import User


class NoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'url', 'title', 'text')


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LocationLog
        fields = ('id', 'url', 'area')