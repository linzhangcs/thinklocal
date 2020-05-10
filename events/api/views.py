from rest_framework.generics import ListAPIView, RetrieveAPIView
from events.models import Event
from .serializers import EventSerializer


class EventListView(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventDetailView(RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
