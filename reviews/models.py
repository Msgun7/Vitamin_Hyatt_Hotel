from django.db import models


class Review(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    booked = models.ForeignKey('hotels.Book',on_delete=models.CASCADE, related_name='booked_users')
    room = models.ForeignKey('hotels.Rooms', on_delete=models.CASCADE, related_name='reviews')
    title = models.CharField(max_length=50)
    context = models.TextField(max_length=255)
    STAR_CHOICES = (
        (1, '1점'),
        (2, '2점'),
        (3, '3점'),
        (4, '4점'),
        (5, '5점'),
    )
    stars = models.PositiveIntegerField(choices=STAR_CHOICES, default=0)
    point = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)
