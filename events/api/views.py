from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from events.models import *
from .serializers import *
from django.core import serializers
import json


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    # permissions_classes = [permissions.IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permissions_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['post'])
    def check_password(self, request):
        data = request.data
        in_email = data["email"]
        input_password = data["password"].strip()

        user = User.objects.filter(email=in_email)
        if user:
            user = user[0]
            user_json = serializers.serialize("json", [user, ])
            user_json = json.loads(user_json)
            user_json = user_json[0]
            user_json['status'] = "password matches"
            if user.password == input_password:
                return Response(user_json)
            else:
                return Response({'status': 'password does not match'})
        else:
            return Response({'status': 'email is not found'})


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    # permissions_classes = [permissions.IsAuthenticated]


class GroupOrganizerViewSet(viewsets.ModelViewSet):
    queryset = GroupOrganizer.objects.all()
    serializer_class = GroupOrganizerSerializer
    # permissions_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['post'])
    def getGroups(self, request):
        data = request.data
        user_id = data["userId"]
        groups = GroupOrganizer.objects.filter(organizer=user_id)
        groupsJson = []

        for group in groups:
            print(group.group.id)
            print(group.group.group_name)
            group_info = Group.objects.filter(id=group.group.id).first()
            group_json = serializers.serialize("json", [group_info, ])
            group_json = json.loads(group_json)
            group_json = group_json[0]

            groupsJson.append(group_json)

        if groups:
            return Response({"status": "found", "groups": groupsJson})

        else:
            return Response({"status": "Your don't have a group yet"})


class InitiativeViewSet(viewsets.ModelViewSet):
    queryset = Initiative.objects.all()
    serializer_class = InitiativeSerializer
    # permissions_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['post'])
    def getInitiatives(self, request):
        data = request.data
        group_id = data["groupId"]
        initiatives = Initiative.objects.filter(group=group_id)

        for initiative in initiatives:
            print(initiative.name)
            initiatives_json = serializers.serialize("json", initiatives)
            initiatives_json = json.loads(initiatives_json)

        if initiatives:
            return Response({"status": "found", "initiatives": initiatives_json})

        else:
            return Response({"status": "Your don't have a group yet"})


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    # permissions_classes = [permissions.IsAuthenticated]


class AttendeeViewSet(viewsets.ModelViewSet):
    queryset = Attendee.objects.all()
    serializer_class = AttendeeSerializer
    # permissions_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['post'])
    def getAttendeeInfo(self, request):
        data = request.data
        input_event_id = data["eventId"]
        userIds = Attendee.objects.filter(event_id=input_event_id)
        userNames = []

        for user in userIds:
            # print(User.objects.filter(id=user.user))
            print(user.user.user_name, type(user.user.user_name))
            userNames.append(user.user.user_name)

        if userIds:
            return Response({"status": "found", "users": userNames})

        else:
            return Response({"status": "No one joined yet"})
