from django.shortcuts import render, redirect, reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User


def index(request):
    room_name = "your_room_name"
    return render(request, "chat/index.html", {"room_name": room_name})


def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})


def register(request):
    # if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse('login'))
    else:
        context = {'form': form}
        return render(request, 'registration/register.html', context)
