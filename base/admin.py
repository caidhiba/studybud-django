from django.contrib import admin

# Register your models here.

from .models import Room,Topic,Message
#we have to this to be able to see the model room

admin.site.register(Room) #after writing this instruction in the panel ill notice a new base room
admin.site.register(Topic)
admin.site.register(Message)

