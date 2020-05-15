from events.models import Event
from rest_framework import serializers


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ("event_title", "event_date",
                  "event_description", "event_creator",
                  "initiative", "group")
