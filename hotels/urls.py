from django.urls import path, include
from hotels import views
from Vitamin_Hyatt import settings
from django.conf.urls.static import static

urlpatterns = [
    path('rooms/book/<int:pk>/',views.BookManage.as_view(), name='book'),
    path('rooms/', views.RoomView.as_view(), name='rooms_view'),
    path('rooms/spot/', views.SpotViewAPI.as_view(), name='spot_view'),
    path('rooms/spot/<int:spot_id>/', views.SpotViewAPI.as_view(), name='spot_detail_view'),
    path('rooms/<int:room_id>/', views.DetailRoomViewAPI.as_view(), name='detail_room_view'),
    path('customers/<int:room_id>/', views.BookUsersViewAPI.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

