from django.shortcuts import render, redirect


def index(request):
    # Logic to fetch or generate room_name
    room_name = "your_room_name"  # Replace with your logic
    return render(request, "chat/index.html", {"room_name": room_name})


def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})

