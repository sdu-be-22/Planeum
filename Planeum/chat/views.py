from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.shortcuts import redirect, render
from Planeum.settings import MEDIA_URL
from chat.models import Room, Message
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def chathome(request):
    rooms = Room.objects.all()
    return render(request,'chathome.html',{'allrooms':rooms})

@login_required
def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {
        'username':username,
        'room':room,
        'room_details':room_details
    })

def checkview(request):
    typed = request.POST['room_name']
    selected = request.POST['select_room']

    if typed != '':
        path = '/chat/'+typed+'/?username='+request.user.username
        if Room.objects.filter(name=typed).exists():
            return HttpResponseBadRequest("Room already exists")
        else:
            new_room = Room.objects.create(name=typed)
            new_room.save()
            return redirect(path)
    elif selected != '':
        path = '/chat/'+selected+'/?username='+request.user.username
        if Room.objects.filter(name=selected).exists():
            return redirect(path)
        else:
            new_room = Room.objects.create(name=selected)
            new_room.save()
            return redirect(path)
    else: return chathome(request)

@csrf_protect
def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']
    f = request.FILES.get('mfile')
    new_message = Message.objects.create(value=message, user=username, room=room_id, file=f)
    new_message.save()
    return HttpResponse("Message send successfuly")


def get_messages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})
