from django.shortcuts import render
from django.http import HttpResponse

#to render the models from the database

from .models import Room

rooms = [
    {'id':1, 'name':'lets learn python'},
    {'id':2, 'name':'design with me'},
    {'id':3, 'name':'frontend developper'},
]

# the request is an http object that gonna tell us what kind of method is sent what kind of data what is the 
# user sending to the backend
# Create your views here.
def home(request):

    rooms = Room.objects.all()
    # return HttpResponse('home page');
    # that third parametre is how would be addressing the python list in the template above and the list we are passing in,
    #by adding this parametre we have access to the list rooms inside of the template

    # we can name that 3rd parametre as context and pass it so it can be more readable
    context = {'rooms':rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    # room = None
    # for i in rooms:
    #     if i['id'] == int(pk):
    #         room = i #here means if the primary key of url we just clcicked matches one of room ids
    room = Room.objects.get(id = pk)
    context = {'room':room}
    # return HttpResponse('room')
    return render(request, 'base/room.html', context)

def createRoom(request):
    return render(request, 'base/room_form.html')