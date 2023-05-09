from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    # path('users/', include("users.urls")),
    path('manager/', include("hotels.urls")),
=======
    path('users/', include('users.urls')),
>>>>>>> 9a70122 (add user model)
]
