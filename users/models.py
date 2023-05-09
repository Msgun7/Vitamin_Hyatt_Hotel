from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from hotels.models import Rooms, Book






class UserManager(BaseUserManager): 
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None): 
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
    
class User(AbstractBaseUser): 
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    username = models.CharField(max_length=255,null=False) 
    phone = models.CharField(max_length=255,null=False) 
    point = models.IntegerField(default= 0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booked = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='booked_users')
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    context = models.TextField(max_length=255)
    stars = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title