from django.db import models


# Create your models here.
class User():
    pass


class Review():
    # room
    user = models.ForeignKey(User, on_delete=models.CASCADE) #나중에 추가 
    # booked
    title = models.CharField(max_length=100)
    content = models.TextField()
    stars = models.IntegerChoices([1, 2, 3, 4, 5] , null=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title