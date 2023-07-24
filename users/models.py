from django.contrib.auth.models import AbstractUser
from django.db import models

from users.services import UserCManager
from django.utils.translation import gettext_lazy as _
NULLABLE = {'null': True, 'blank': True}

class UserRoles(models.TextChoices):
    MEMBER = 'member', _('member')
    MODERATOR = 'moderator', _('moderator')

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    city = models.CharField(max_length=100, verbose_name='Город', **NULLABLE)
    role = models.CharField(max_length=10, choices=UserRoles.choices, default=UserRoles.MEMBER, verbose_name='роль',
                            **NULLABLE)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserCManager()

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
