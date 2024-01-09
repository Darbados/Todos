from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, PermissionsMixin, User, UserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


class TodoUserManager(UserManager):
    pass


class TodoUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_("Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."),
        error_messages={"unique": _("A user with that username already exists.")},
        null=True,
        blank=True,
    )

    objects = TodoUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email}, date joined: {self.date_joined}"
