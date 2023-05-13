from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('profile/<int:user_id>/', views.UserProfileView.as_view(), name='profile'),
    path('mypagelist/<int:pk>/', views.MyPage.as_view(), name='mypagelist'),
    path('myreservation/<int:booked_id>/', views.MyBookReviewCreate.as_view()),
    path('myreservation/Detail/<int:review_id>/', views.ReviewDetail.as_view())
]
