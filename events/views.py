from django.shortcuts import render
from .models import Event
# Create your views here.

def index(request):
    latest_event_list = Event.objects.order_by('-event_date')[:5]
    context = {'latest_event_list': latest_event_list}
    return render(request, 'events/index.html', context)

# show specific event details

def detail(request, event_id):
    try:
        event = Event.objects.get(pk = event_id)
    except Event.DoesNotExist:
        raise Http404('Event does not exist')
    return render(request, 'events/detail.html', {'event':event})