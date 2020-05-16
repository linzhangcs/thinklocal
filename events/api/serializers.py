from events.models import *
from rest_framework import serializers


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ("id", "event_title", "event_date",
                  "event_description", "event_creator",
                  "initiative", "group")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "user_name", "first_name",
                  "last_name", "email",
                  "zipcode", "join_reason", "password")


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("id", "create_date", "create_by",
                  "group_name", "creator")


class GroupOrganizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupOrganizer
        fields = ("id", "organizer", "group")


class InitiativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Initiative
        fields = ("id", "name", "group",
                  "create_date", "create_by")


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ("id", "group", "user")


class AttendeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendee
        fields = ("id", "event", "user")
