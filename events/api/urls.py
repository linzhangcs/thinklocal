from django.urls import path, include
from rest_framework import routers
from .views import EventListView, EventDetailView, EventViewSet

app_name = "api"

router = routers.DefaultRouter()
router.register(r'events', EventViewSet)
urlpatterns = [
    path('', include(router.urls))
    # path('api-auth/', include('rest_framework.urls',
    #                           namespace='rest_framework'))
    # path('', EventListView.as_view()),
    # path('<pk>', EventListView.as_view())
]
