from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"null": True, "blank": True}


class User(AbstractUser):
    """Модель для создания пользователя"""
    username = None

    email = models.EmailField(unique=True, verbose_name="email")
    avatar = models.ImageField(
        upload_to="users/avatars/", verbose_name="аватар", **NULLABLE
    )
    phone = models.CharField(max_length=50, verbose_name="номер", **NULLABLE)

    tg_chat_id = models.CharField(max_length=30, verbose_name='id TG-чата', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
