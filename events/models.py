from django.db import models

DEFAULT_FK_ID = 1


class User(models.Model):
    user_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    zipcode = models.CharField(max_length=20)
    join_reason = models.CharField(max_length=500)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.user_name


class Group(models.Model):
    create_date = models.DateTimeField()
    create_by = models.CharField(max_length=200)
    group_name = models.CharField(max_length=200)
    creator = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, default=DEFAULT_FK_ID)

    def __str__(self):
        return self.group_name + ": " + self.create_by


class GroupOrganizer(models.Model):
    organizer = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, default=DEFAULT_FK_ID)
    group = models.ForeignKey(Group, on_delete=models.DO_NOTHING)


class Initiative(models.Model):
    name = models.CharField(max_length=2000)
    group = models.ForeignKey(
        Group, on_delete=models.DO_NOTHING, default=DEFAULT_FK_ID)
    create_date = models.DateTimeField()
    create_by = models.CharField(max_length=200)

    def __str__(self):
        return self.name + ": " + self.create_by


class Member(models.Model):
    group = models.ForeignKey(Group, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)


class Event(models.Model):
    event_title = models.CharField(max_length=2000)
    event_date = models.DateTimeField('event date')
    event_description = models.TextField()
    event_creator = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, default=DEFAULT_FK_ID)
    initiative = models.ForeignKey(
        Initiative, on_delete=models.DO_NOTHING, default=DEFAULT_FK_ID)
    group = models.ForeignKey(
        Group, on_delete=models.DO_NOTHING, default=DEFAULT_FK_ID)

    def __str__(self):
        return self.event_title + ": " + self.event_description


class Attendee(models.Model):
    event = models.ForeignKey(Event, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
