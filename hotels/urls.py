from django.urls import path
from hotels import views

urlpatterns = [
    path('rooms/', views.RoomViewAPI.as_view(), name='rooms_view'),
    path('rooms/spot/', views.SpotViewAPI.as_view()),
    path('rooms/spot/<int:spot_id>', views.SpotViewAPI.as_view()),
    path('rooms/<int:room_id>/', views.DetailRoomViewAPI.as_view()),
    path('customers/<int:room_id>/', views.BookUsersViewAPI.as_view()),
]
