from django.shortcuts import render
from django.shortcuts import reverse
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm

from .utils import registered_required


def home(request):
    room_name = "your_room_name"
    return render(request, "chat/home.html", {"room_name": room_name})


@registered_required
def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})


def register(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse('login'))
    else:
        context = {'form': form}
        return render(request, 'registration/register.html', context)
