from django.urls import path, include
from rest_framework import routers
from .views import *

app_name = "api"

router = routers.DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'group-organizers', GroupOrganizerViewSet)
router.register(r'initiatives', InitiativeViewSet)
router.register(r'members', MemberViewSet)
router.register(r'attendees', AttendeeViewSet)

urlpatterns = [
    path('', include(router.urls))
    # path('api-auth/', include('rest_framework.urls',
    #                           namespace='rest_framework'))
    # path('', EventListView.as_view()),
    # path('<pk>', EventListView.as_view())
]
