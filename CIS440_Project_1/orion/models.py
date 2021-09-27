from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    attendees = models.TextField(default='') # will be a JSON string 
    date_of_event = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE) # on_delete=CASCADE --> when a user is deleted, all of their events will be deleted as well
    