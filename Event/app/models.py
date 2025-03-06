from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Band(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    start_date = models.DateField()
    Number_of_events = models.IntegerField()
    def __str__(self):
        return f'{self.name} - {self.country}'

class Event(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    poster = models.ImageField(upload_to='media/')
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    band = models.ForeignKey(Band, on_delete=models.CASCADE,null=True, blank=True)
    isOpen = models.BooleanField(default=False,null=True,blank=True)
    def __str__(self):
        return f'{self.name} - {self.date}'

class BandEvent(models.Model):
    band = models.ForeignKey(Band, on_delete=models.CASCADE,null=True, blank=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE,null=True, blank=True)


