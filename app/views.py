from django.shortcuts import render, redirect


def index(request):
    return render(request, "chat/index.html")


def room(request):
    if request.method == 'GET':
        new_room_number = request.GET.get('room_number')
        if new_room_number:
            return redirect('room')
    return render(request, "chat/room.html")

