from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# a room can only have one topic so its onetomany relationship between topic and room
class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Room(models.Model):
    host= models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)#if we place the class topic under the
    #  class room we would have to make the parametre topic in a string like 'topic' s it can work
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    # participants = (that stores all the users that are currently active in our room)
    updated = models.DateTimeField(auto_now=True)
    # the diff between now and now_add is that now takes a screenshot of the time everytime the update 
    # happens but the other one takes the time only in the first time the action of the creation happens
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

#    __str__ is a magic method in Python that returns a string representation of an object.
# self.name refers to an attribute of the class, which is assumed to exist in the model.
# When you call str(instance) or display the object in an interface like the Django admin panel, 
# it will return the name attribute instead of something generic like <ModelName object (1)>.

class Message(models.Model):
    # there is another onetomany relationship between user and message bcs user can type many msgs so we do 
    # the same thing after importing the user pannel from django above
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # this is a oneToMany relationship between romm and message, the attribute ondelete means if the parent grts
    #deleted , if we choose cascade means the child gets deleted too otherwise it still stays in the data base 
    # if we choose set_null
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]
    
