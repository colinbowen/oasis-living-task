from django.contrib import admin
from .models import Note, LocationLog, User

# Register your models here.
admin.site.register(Note)
admin.site.register(LocationLog)
admin.site.register(User)