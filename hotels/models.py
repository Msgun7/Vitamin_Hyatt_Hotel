from django.db import models
from django.urls import reverse
from users.models import User
from django.core.validators import MinLengthValidator, MinValueValidator
from .validators import contains_special_character, validate_phone_number


class Spots(models.Model):
    name = models.CharField(max_length=100, unique=True, validators=[
        contains_special_character])
    call_number = models.CharField(validators=[validate_phone_number], max_length=20, unique=True)

    location = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse('spot_detail_view', kwargs={'spot_id': self.id})

    def __str__(self):
        return self.name


# null, blank
class Rooms(models.Model):
    all_status = [
        ('checkin', 'checkin'),
        ('empty', 'empty'),
    ]
    spot = models.ForeignKey(Spots, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, validators=[
        contains_special_character])
    description = models.TextField(max_length=300, validators=[
        MinLengthValidator(10)], error_messages="10자 이상 입력하셔야합니다.")
    image = models.ImageField(null=True, blank=True)
    price = models.IntegerField(validators=[MinValueValidator(0)], null=False)
    max_members = models.IntegerField()
    status = models.CharField(choices=all_status, max_length=10)

    def get_absolute_url(self):
        return reverse('detail_room_view', kwargs={'room_id': self.id})

    def __str__(self):
        return self.name


class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(
        Rooms, on_delete=models.CASCADE, related_name='bookset')
    created_at = models.DateTimeField(auto_now_add=True)
    members = models.IntegerField(default=1)
    check_in = models.DateField() 
    check_out = models.DateField()

    def __str__(self):
        return self.room.name
