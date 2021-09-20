from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_of_event = models.DateTimeField()
    time_of_event = models.TimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE) # on_delete=CASCADE --> when a user is deleted, all of their events will be deleted as well
