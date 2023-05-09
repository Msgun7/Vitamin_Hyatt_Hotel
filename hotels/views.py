from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Rooms
from hotels.serializers import RoomSerializer
# Create your views here.


class RoomView(APIView):
    def get(self, request):
        # 모든 방들의 대한 정보를 불러옴
        rooms = Rooms.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response((serializer.data), status=status.HTTP_200_OK)
    
    def post(self, request):
        # 방을 추가
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, room_id):
        # 방을 삭제 
        room = get_object_or_404(Rooms, id= room_id)
        room.delete()
        return Response('삭제됨', status=status.HTTP_204_NO_CONTENT)

    

class Book(APIView):
    def get(self, request):
        pass

    def post(self, request):
        # 예약하기 
        pass

    def delete(self, request, user_id):
        # 예약을 취소하기 
        pass
