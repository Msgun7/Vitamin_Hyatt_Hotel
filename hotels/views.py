from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from hotels.models import Rooms
from hotels.serializers import RoomsSerializers

class RoomViewAPI(APIView):
    def post(self, request):
        serializer = RoomsSerializers(data = request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        rooms = Rooms.objects.all()
        serializer = RoomsSerializers (rooms, many=True)
        return Response(serializer.data)


class DetailRoomViewAPI():
    pass


class BookUsersViewAPI():
    pass


class SpotViewAPI():
    pass

