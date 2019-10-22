from rest_framework import serializers
from .models import Note, User, LocationLog

class NoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'url', 'title', 'text')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'first_name', 'last_name', 'email')


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source=User.email, read_only=True)
    class Meta:
        model = LocationLog
        fields = ('id', 'url', 'area', 'user')