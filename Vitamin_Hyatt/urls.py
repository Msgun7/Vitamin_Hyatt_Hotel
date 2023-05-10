from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    path('manager/', include("hotels.urls")),
    path('users/', include('users.urls')),
=======
    path('users/', include('users.urls')),
    path('manager/', include("hotels.urls")),
>>>>>>> 0dcc30a (fix hetels.view)
=======
=======
>>>>>>> fc034b8 (fix hetels.view)
=======
>>>>>>> 2003d31 (fix hetels.view)
    path('users/', include('users.urls')),
=======
=======
>>>>>>> 3afe058 (add user model)
    # path('users/', include("users.urls")),
>>>>>>> ff383e3 (merge)
    path('manager/', include("hotels.urls")),
=======
<<<<<<< HEAD
    path('users/', include("users.urls")),
    path('managers/', include("managers.urls")),
>>>>>>> 475ffb0 (Views 방 등록 조회)
<<<<<<< HEAD
>>>>>>> 41c6c1e (fix hetels.view)
=======
=======
    path('users/', include('users.urls')),
>>>>>>> 9a70122 (add user model)
>>>>>>> 3afe058 (add user model)
>>>>>>> 2003d31 (fix hetels.view)
]
