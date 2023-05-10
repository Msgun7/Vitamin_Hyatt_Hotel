from django.db import models
from django.urls import reverse
from users.models import User 

class Spots(models.Model):
    name = models.CharField(max_length=100, unique=True)
    call_number = models.CharField(max_length=100)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# null, blank
class Rooms(models.Model):
    all_status = [
        ('checkin', 'checkin'),
        ('empty', 'empty'),
    ]
    spot = models.ForeignKey(Spots, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    # image = models.ImageField()
    price = models.IntegerField()
    max_members = models.IntegerField()
    status = models.CharField(choices=all_status, max_length=10)

    def get_absolute_url(self):
        return reverse('todo_detail_view', kwargs={'room_id': self.id})

    def __str__(self):
        return self.name



class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now=True)
    members = models.IntegerField()
    check_in = models.DateField(auto_now=True)
    check_out = models.DateField(auto_now=True)
