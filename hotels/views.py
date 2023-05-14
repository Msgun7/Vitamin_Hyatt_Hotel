from .serializers import DetailSerializer, RoomsSerializer, SpotSerializer, BookSerializer
from rest_framework.generics import get_object_or_404
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Rooms, Book, Spots
from hotels.serializers import RoomsSerializer, BookSerializer, DetailSerializer , SpotSerializer,BookUserListSerializer , RoomStarSerializer
# Create your views here.
from datetime import date
from django.db.models import Avg
from users.models import AdminUser


class RoomView(APIView):
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        admin = get_object_or_404(AdminUser, admin_user=request.user)
        rooms = Rooms.objects.filter(spot=admin.spot)
        serializer = RoomsSerializer(rooms, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = RoomsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 방 정보 수정 및 삭제
class DetailRoomViewAPI(APIView):
    # permission_classes = [permissions.IsAuthenticated]
    def get_object(self, request, room_id):
        room = get_object_or_404(Rooms, id=room_id)
        return room

    def get(self, request, room_id):
        room = get_object_or_404(Rooms, id=room_id)
        serializer = DetailSerializer(room)
        return Response(serializer.data, status=status.HTTP_200_OK)

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
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, room_id):

        admin = get_object_or_404(AdminUser, admin_user=request.user)
        booked_all_rooms = get_object_or_404(Rooms, id=room_id, spot=admin.spot)
        serializer = BookUserListSerializer(booked_all_rooms)
        return Response(serializer.data, status=status.HTTP_200_OK)

class BookUserCal(APIView):
    def get(self, request, room_id):
        booked_all_rooms = get_object_or_404(Rooms, id=room_id)
        serializer = BookUserListSerializer(booked_all_rooms)
        return Response(serializer.data, status=status.HTTP_200_OK)


# 지점 생성 및 조회
class SpotViewAPI(APIView):
    # permission_classes = [permissions.IsAuthenticated]
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
        room = get_object_or_404(Rooms, id=pk)
        serializer = BookSerializer(data = request.data)
        all_checkins = room.bookset.filter() # 그 방이 가지고 있는 모든 예약들
        checkin_y_m_d = list(map(int, request.data["check_in"].split('-')))
        checkout_y_m_d = list(map(int, request.data["check_out"].split('-')))
        my_check_in = date(checkin_y_m_d[0], checkin_y_m_d[1],checkin_y_m_d[2])
        my_check_out = date(checkout_y_m_d[0],checkout_y_m_d[1],checkout_y_m_d[2])
        
        for i in all_checkins:
            print(f'{bool((my_check_in)>=(i.check_in))}')
            if my_check_in < i.check_in:  #체크인 날짜가 적절할 경우
                pass
                if my_check_out <= i.check_in:  # 체크 아웃 날짜가 적절한 경우
                    pass
                elif my_check_out > i.check_in:
                    return Response(f"예약 할 수 없음, 나의 예약 {my_check_in}~{my_check_out}, 이미 예약된 날짜 {i.check_in}~{i.check_out}")

            elif my_check_in >= i.check_in:  # 체크아웃 날짜가 적절하지 않을 경우
                if i.check_out <= my_check_in :
                    pass
                elif i.check_out > my_check_in:
                    return Response(f"예약 할 수 없음, 나의 예약 {my_check_in}~{my_check_out}, 이미 예약된 날짜 {i.check_in}~{i.check_out}")

            
        if serializer.is_valid():
            serializer.save(user=request.user, room=room)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)
   
   
    def delete(self, request, pk):
        book = get_object_or_404(Book, id=pk)
        if request.user == book.user:
            book.delete()
            return Response("예약 취소됨", status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("권한이 없음")


class RoomViewBySpot(APIView):
    def get(self, request, spot_id):
        rooms_in_spot = Rooms.objects.filter(spot=spot_id)
        avg_star = rooms_in_spot.prefetch_related('review_set').aggregate(Avg('review_set__stars'))['review_set__stars__avg']
        serializer = RoomStarSerializer(rooms_in_spot, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
