from django.urls import path
from hotels import views

urlpatterns = [
    path('rooms/', views.RoomViewAPI.as_view(), name = 'add_rooms'),
    path('rooms/', views.RoomViewAPI.as_view(), name = 'search_rooms'),
]