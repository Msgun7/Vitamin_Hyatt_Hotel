from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from .validators import check_password, check_username
from hotels.validators import validate_phone_number


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
    password = models.CharField(max_length=100, validators=[check_password])
    username = models.CharField(max_length=255,null=False, validators=[check_username]) 
    phone = models.CharField(validators=[validate_phone_number], max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    point = models.IntegerField(blank=True, default= 0)
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


class AdminUser(models.Model): 
    admin_user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_staff = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=True)
    # 지점 넣어도 될까요? 넣어서 방 수정하거나 생성할 때 자기 지점꺼만 할 수 있다던가 그런,,,
    
    def __str__(self):
        return self.admin_user.email




