from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)
from django.db import models
from django.utils.translation import gettext_lazy as _
from .validators import phone_number_regex

class UserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('The Phone Number field must be set')
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(phone_number, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(
        verbose_name=_('phone number'),
        max_length=11,
        unique=True,
        validators=[
            phone_number_regex,
        ],
    )
    first_name = models.CharField(
        verbose_name=_('first name'),
        max_length=32,
        blank=True,
    )
    last_name = models.CharField(
        verbose_name=_('last name'),
        max_length=32,
        blank=True,
    )
    is_active = models.BooleanField(
        default=True,
    )
    is_staff = models.BooleanField(
        default=False,
    )

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    class Meta:
        indexes = [
            models.Index(fields=["phone_number"]),
        ]

    def __str__(self):
        return self.phone_number