from django.urls import path
from users import views

urlpatterns = [
    path('signup/',views.UserView.as_view(), name='signup'),
    path('login/', views.CustomTokenObtainPairView.as_view(), name='login'),  
    path('profile/', views.UserProfileView.as_view(), name='profile'),
]