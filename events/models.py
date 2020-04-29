from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.user_name

class Event(models.Model):
    event_title = models.CharField(max_length=2000)
    event_date = models.DateTimeField('event date')
    event_description = models.TextField()
    organizer = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.event_title +" "+ self.event_description

class Attendee(models.Model):
    event = models.ForeignKey(Event, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
