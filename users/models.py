from django.db import models


class Review(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    booked = models.ForeignKey('book.Book', on_delete=models.CASCADE, related_name='booked_users')
    room = models.ForeignKey('rooms.Rooms', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    context = models.TextField(max_length=255)
    stars = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

