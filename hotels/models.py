from django.db import models
from django import reverse

class Book(models.Model):
    # user = models.ForeignKey(Users, on_delete=models.CASCADE)
    # room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    members = models.IntegerField(default=1)
    check_in = models.DateField()
    check_out = models.DateField()
    
    # def __str__(self):
    #     return self.user
