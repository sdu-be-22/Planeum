from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from chat.models import Room, Message
# Create your views here.
def chathome(request):
    return render(request, 'chathome.html')

def room(request, room):
    username = request.GET.get('username')
    room_datails = Room.objects.get(name=room)
    return render(request, 'room.html', {
        'username':username,
        'room':room,
        'room_datails':room_datails
    })

def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/chat/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/chat/'+room+'/?username='+username)

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse("Message send successfuly")
    
def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})