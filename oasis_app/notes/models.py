from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager


# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class LocationLog(models.Model):
    area = models.CharField(max_length=100)
    timestamp = models.CharField(max_length=100)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.area, self.timestamp

