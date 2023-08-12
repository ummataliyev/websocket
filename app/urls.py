from django.urls import path

from .views import index
from .views import room


urlpatterns = [
    path("", index, name="index"),
    path("room/", room, name="room")
]
