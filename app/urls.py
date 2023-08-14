from django.urls import path

from django.contrib.auth.views import LoginView
from .views import index, register
from .views import room


urlpatterns = [
    path("", index, name="index"),
    path('room/<str:room_name>/', room, name='room'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', register, name='register'),

]
