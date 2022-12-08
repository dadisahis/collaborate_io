from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.name
    


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    participants = models.ManyToManyField(User,related_name='participants',blank=True) 
    updated = models.DateTimeField(auto_now=True) # Difference between autoNow and autoNow_add auto_now saves timestamp each time the object is updated whereas auto_now_add only saves timestamp when an object is created
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-updated','-created'] #the '-' symbol means the ordering in descending order and no '-' means ascending order
    
    def __str__(self) -> str:
        return str(self.name)
    

class Message(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE) #If a room is deleted, all the children records should be deleted using models.CASCADE command
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True) # Difference between autoNow and autoNow_add auto_now saves timestamp each time the object is updated whereas auto_now_add only saves timestamp when an object is created
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-updated','-created']
    
    def __str__(self) -> str:
        return str(self.body[:50])
    