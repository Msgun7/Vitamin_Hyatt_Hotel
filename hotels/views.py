from .serializers import DetailSerializer, RoomsSerializers, SpotSerializer
from rest_framework.generics import get_object_or_404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Rooms, Book, Spots




class RoomViewAPI():
    def post(self, request):
        serializer = RoomsSerializers(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        rooms = Rooms.objects.all()
        serializer = RoomsSerializers(rooms, many=True)
        return Response(serializer.data)
      

# 방 정보 수정 및 삭제
class DetailRoomViewAPI(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get_object(self, request, room_id):
        room = get_object_or_404(Rooms, id=room_id, user=request.user)
        return room

    def put(self, request, room_id):
        room = self.get_object(request, room_id)
        serializer = DetailSerializer(room, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, room_id):
        pass



class BookUsersViewAPI(APIView):
    def get(self, request, room_id):
        booked_all_rooms = get_object_or_404(Book, id=room_id)
        serializer = RoomsSerializers(booked_all_rooms, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SpotViewAPI(APIView):
    def get(self, request):
        spots = Spots.objects.all()
        serializer = SpotSerializer(spots, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = SpotSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


