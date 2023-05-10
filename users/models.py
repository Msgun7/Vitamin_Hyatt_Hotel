from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


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
    username = models.CharField(max_length=255, null=False)
    phone = models.CharField(max_length=255, null=False)
    point = models.IntegerField(default=0)
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

    def __str__(self):
        return str(self.title)



class Review():
    # room
    user = models.ForeignKey() #나중에 추가 
    # booked
    title = models.CharField()
    content = models.TextField()
    stars = models.IntegerChoices([1, 2, 3, 4, 5] , null=True)
    create_at = models.DateTimeField(auto_now_add=True)

