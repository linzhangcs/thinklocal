from django.urls import path
from .views import EventListView, EventDetailView

app_name = "api"
urlpatterns = [
    path('', EventListView.as_view()),
    path('<pk>', EventListView.as_view())
]
