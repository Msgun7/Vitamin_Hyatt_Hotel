from django.db import models


# Create your models here.
class User():
    pass


class Review():
    # room
    user = models.ForeignKey() #나중에 추가 
    # booked
    title = models.CharField()
    content = models.TextField()
    stars = models.IntegerChoices([1, 2, 3, 4, 5] , null=True)
    create_at = models.DateTimeField(auto_now_add=True)