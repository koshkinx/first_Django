from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        """
        Create and return a regular user with a username and password.
        """
        if not username:
            raise ValueError('The username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        """
        Create and return a superuser with a username and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(username, password, **extra_fields)

    def get_by_natural_key(self, username):
        """
        Retrieve a user by their natural key (username).
        """
        return self.get(username=username)


class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=150, unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    def has_module_perms(self, app_label):
        """
        Проверяет, имеет ли пользователь разрешения на просмотр приложения с указанным меткой.
        """
        return True

    def has_perm(self, perm, obj=None):
        """
        Проверяет, имеет ли пользователь указанное разрешение.
        """
        return True
    USERNAME_FIELD = 'username'
    # Fields required when creating a user via the createsuperuser command
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


class UserProfile(models.Model):
    bio = models.CharField(max_length=150, null=True, blank=True)
    phone_number = models.CharField(max_length=10, null=True, blank=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
