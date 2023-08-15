from django.urls import path

from .views import home
from .views import room
from .views import register
from django.contrib.auth.views import LoginView


urlpatterns = [
    path("", home, name="home"),
    path('room/<str:room_name>/', room, name='room'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', register, name='register')

]
