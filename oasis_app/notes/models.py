from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name, self.last_name


class Note(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class LocationLog(models.Model):
    area = models.CharField(max_length=100)
    timestamp = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.area, self.timestamp

