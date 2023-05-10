from django.db import models


class User(models.Model):
    name = models.CharField(max_length=20)
  
    def __str__(self):
        return str(self.name)

class Review(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    booked = models.ForeignKey('rooms.Book',on_delete=models.CASCADE, related_name='booked_users')
    room = models.ForeignKey('rooms.Rooms', on_delete=models.CASCADE, related_name='reviews')
    title = models.CharField(max_length=50)
    context = models.TextField(max_length=255)
    stars = models.PositiveIntegerField(default=0)
    point = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.title)