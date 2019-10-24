from django.urls import path, include
from . import views
from rest_framework import routers, viewsets

router = routers.DefaultRouter()
router.register('notes', views.NoteView)
router.register('locations', views.LocationLogView)
router.register(r'users', views.UserView)



urlpatterns = [
    path('', include(router.urls))
]