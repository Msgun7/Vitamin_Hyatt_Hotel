from django.urls import path
<<<<<<< HEAD
from users import views
=======
<<<<<<< HEAD
from . import views
>>>>>>> 2003d31 (fix hetels.view)

urlpatterns = [
    path('signup/',views.UserView.as_view(), name='signup'),
    path('login/', views.CustomTokenObtainPairView.as_view(), name='login'),  
    path('profile/', views.UserProfileView.as_view(), name='profile'),
    path('<int:room_id>', views.RoomDetailReviewList.as_view()),
    path('reviews/<int:review_id>', views.ReviewDetail.as_view()),
    path('profile/<int:user_id>', views.MyPage.as_view())
]
<<<<<<< HEAD

=======
=======
from users import views

urlpatterns = [
    path('signup/',views.UserView.as_view(), name='signup'),
    path('login/', views.CustomTokenObtainPairView.as_view(), name='login'),  
    path('profile/', views.UserProfileView.as_view(), name='profile'),
]
>>>>>>> 3afe058 (add user model)
>>>>>>> 2003d31 (fix hetels.view)
