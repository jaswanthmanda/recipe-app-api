"""
Database models
"""

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    """Manager for user

    Args:
        BaseUserManager (_type_): _description_
    """

    def create_user(self, email, password=None, **extra_field):
        """Create, save and return a new user."""
        user = self.model(email=email, **extra_field)
        user.set_password(password)
        user.save(using=self._db)


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = "email"