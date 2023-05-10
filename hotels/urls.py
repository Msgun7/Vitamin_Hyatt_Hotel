from django.urls import path, include
from hotels import views

urlpatterns = [
<<<<<<< HEAD
    path('rooms/', views.RoomViewAPI.as_view(), name='rooms_view'),
    path('rooms/spot/', views.SpotViewAPI.as_view()),
    path('rooms/spot/<int:spot_id>', views.SpotViewAPI.as_view()),
=======
<<<<<<< HEAD
>>>>>>> 41c6c1e (fix hetels.view)
    path('book/',views.RoomView.as_view(), name='book'),
    path('rooms/<int:room_id>/', views.DetailRoomViewAPI.as_view()),
    path('customers/<int:room_id>/', views.BookUsersViewAPI.as_view()),
]

=======
    path('rooms/', views.RoomViewAPI.as_view(), name = 'add_rooms'),
    path('rooms/', views.RoomViewAPI.as_view(), name = 'search_rooms'),
]
>>>>>>> 475ffb0 (Views 방 등록 조회)
