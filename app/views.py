from django.shortcuts import render


def index(request):
    room_name = "your_room_name"
    return render(request, "chat/index.html", {"room_name": room_name})


def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})
