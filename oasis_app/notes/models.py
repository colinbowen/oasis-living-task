from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.contrib.auth.models import User


# Create your models here.
'''
class NoteList(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
'''


class Note(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # note_list = models.ForeignKey(NoteList, related_name='notes', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class LocationLog(models.Model):
    area = models.CharField(max_length=100)
    timestamp = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.area, self.timestamp

