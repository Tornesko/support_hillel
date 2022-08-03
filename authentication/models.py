from django.contrib.auth.models import (  # isort: skip
    AbstractBaseUser,  # isort: skip
    PermissionsMixin,  # isort: skip
    UserManager,  # isort: skip
)  # isort: skip
from django.db import models
from shared.django import TimeStampMixin

# Create your models here.


class CustomUserManager(UserManager):
    def create_user(self, email, username=None, password=None, **kwargs):
        if not email:
            raise ValueError("Email field is required")
        if not password:
            raise ValueError("Password field is required")

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **kwargs)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, username=None, password=None, **kwargs):
        extra_fields: dict = {"is_superuser": True, "is_active": True, "is_staff": True}

        return self.create_user(email, username, password, **extra_fields)


class Role(TimeStampMixin):
    """ User's role"""
    name = models.CharField(max_length=50)


class User(AbstractBaseUser, PermissionsMixin, TimeStampMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, null=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    age = models.PositiveSmallIntegerField(null=True)
    phone = models.CharField(max_length=13, null=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    # role = models.ForeignKey(null=True, default=)

    objects = CustomUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = EMAIL_FIELD
    REQUIRED_FIELDS = []

    class Meta:
        db_table = "users"
        verbose_name_plural = "Users"
