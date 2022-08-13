from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date

# Create your models here.

class Venue(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    zip_code = models.CharField(max_length=150)
    phone = models.CharField(max_length=10)
    web = models.URLField(max_length=50, blank=True)
    email_address = models.EmailField()
    owner = models.IntegerField(blank=False, default=1)
    image = models.ImageField(blank=True, null=True, upload_to='images/')


    def __str__(self):
        return self.name


class MyClubUser(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()


    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Event(models.Model):
    name = models.CharField(max_length=200)
    event_date = models.DateTimeField()
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    #venue = models.CharField(max_length=200)
    manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(MyClubUser, blank=True)
    approved = models.BooleanField(default=False)


    def __str__(self):
        return self.name


    @property
    def days_till(self):
        today = date.today()
        day_till = self.event_date.date() - today
        days_till_stripped = str(day_till).split(",", 1)[0]
        return days_till_stripped


    @property
    def is_past(self):
        today = date.today()
        if self.event_date.date() < today:
            thing = "Past"
        else:
            thing = "Future"
        return thing