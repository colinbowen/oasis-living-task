from django.contrib import admin
from .models import Note, LocationLog

# Register your models here.
admin.site.register(Note)
admin.site.register(LocationLog)