from .serializers import DetailSerializer, RoomsSerializer, SpotSerializer, BookSerializer
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Rooms, Book, Spots
from hotels.serializers import RoomsSerializer, BookSerializer, DetailSerializer , SpotSerializer
# Create your views here.


class RoomView(APIView):
    def get(self, request):
        rooms = Rooms.objects.all()
        serializer = RoomsSerializer(rooms, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RoomsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 방 정보 수정 및 삭제
class DetailRoomViewAPI(APIView):
    # permission_classes = [permissions.IsAuthenticated]
    def get_object(self, request, room_id):
        room = get_object_or_404(Rooms, id=room_id)
        return room

    def patch(self, request, room_id):
        room = self.get_object(request, room_id)
        serializer = DetailSerializer(room, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, room_id):
        room = self.get_object(request, room_id)
        room.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BookUsersViewAPI(APIView):
    def get(self, request, room_id):
        booked_all_rooms = get_object_or_404(Book, id=room_id)
        serializer = RoomsSerializer(booked_all_rooms, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# 지점 생성 및 조회
class SpotViewAPI(APIView):
    def get_object(self, request, spot_id):
        spot = get_object_or_404(Spots, id=spot_id)
        return spot

    def get(self, request, spot_id=None):
        spots = Spots.objects.all()
        serializer = SpotSerializer(spots, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, spot_id=None):
        serializer = SpotSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, spot_id=None):
        spot = self.get_object(request, spot_id)
        serializer = SpotSerializer(spot, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, spot_id=None):
        spot = self.get_object(request, spot_id)
        spot.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BookManage(APIView):
    def get(self, request, pk):
        all_books = get_object_or_404(Book, id=pk)
        serializer = BookSerializer(all_books)
        return Response(serializer.data)

    def post(self, request, pk):
        
        # 예약하기 기능
        # 예약한 방에 같은 날짜의 예약이 없으면 예약 오브젝트 하나 생성
        # 예약 오브젝트는 예약한 사람, 예약한 방, 예약날짜(check_in)을 속성으로 가짐
        print(f"리퀘스트{request.data}")
        room = get_object_or_404(Rooms, id=pk)
        serializer = BookSerializer(data = request.data)
        # room.bookset 뒤에 오브젝트 쓸 필요없음
        # = Book.objects.
        if serializer.is_valid():
            if not room.bookset.filter(room=pk, check_in=request.data["check_in"]).exists():
                serializer.save(user=request.user, room=room)
                # print(f'시리얼라이저{serializer.data}')
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response('예약할 수 없음')
        else:
            return Response(serializer.errors)
       
        # 같은 check_in 이 있으면 예약이 불가합니다.
        # check_in은 날짜 테이블 DateField 입니다.
        # 예를 들어 10일을 예약한다 하면 예약 오브젝트가 10개가 생김...
        # 개선의 여지 ? 
    
    def delete(self, request, pk):
        book = get_object_or_404(Book, id=pk)
        if request.user == book.user:
            book.delete()
            return Response("예약 취소됨", status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("권한이 없음")
        # 예약을 취소하기 


