from django.db import models
from datetime import datetime

from Planeum.settings import MEDIA_ROOT


# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=1000, blank=False, null=False)
class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000)
    room = models.CharField(max_length=1000)
    file = models.ImageField(upload_to="./", blank=True)