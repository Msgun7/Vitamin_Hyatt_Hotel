from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Rooms, Book
from hotels.serializers import RoomSerializer, BookSerializer
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

    
class BookManage(APIView):
    def get(self, request):
        pass

    def post(self, request):
        # 예약하기
        if request.check_in in Book:
            return Response('이미 예약이 잡힌 날짜')
        else :
            serializer = BookSerializer(data = request.data)
            serializer.save()

        return Response('예약을 위한 post 요청')
        # 같은 check_in 이 있으면 예약이 불가합니다.
        # check_in은 날짜 테이블 DateField 입니다.
        # 예를 들어 10일을 예약한다 하면 예약 오브젝트가 10개가 생김...
        # 개선의 여지 ? 

    def delete(self, request, user_id):
        book = get_object_or_404(Book, id=user_id)
        if request.user == book.user:
            book.delete()
            return Response("예약 취소됨", status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("권한이 없음")
        # 예약을 취소하기 
    

class ReserView(APIView):
    pass
