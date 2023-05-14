from django.urls import path
from hotels import views
from Vitamin_Hyatt import settings
from django.conf.urls.static import static

urlpatterns = [
    path('rooms/', views.RoomView.as_view(), name='rooms_view'),
    path('rooms/<int:room_id>/', views.DetailRoomViewAPI.as_view(), name='detail_room_view'),
    path('rooms/spot/', views.SpotViewAPI.as_view(), name='spot_view'),
    path('rooms/spot/<int:spot_id>/', views.SpotViewAPI.as_view(), name='spot_detail_view'),
    path('rooms/book/<int:pk>/',views.BookManage.as_view(), name='book'),
    path('roomsbyspot/<int:spot_id>/', views.RoomViewBySpot.as_view(), name='Rooms_by_spot'),  # 지점별 방 조회
    path('customers/<int:room_id>/', views.BookUsersViewAPI.as_view()),  # 예약자 명단
    path('cal/<int:room_id>/', views.BookUserCal.as_view()),  # 예약 달력
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

