from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('client', 'Müşteri'),
        ('provider', 'Hizmet Sağlayıcı'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, verbose_name='Kullanıcı Tipi')

    def __str__(self):
        return f"{self.username} ({self.get_user_type_display()})"
