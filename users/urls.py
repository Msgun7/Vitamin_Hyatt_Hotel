from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.SignupView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),  
    path('profile/<int:user_id>/', views.UserProfileView.as_view(), name='profile')
#     path('profile/<int:user_id>', views.MyPage.as_view())
]
