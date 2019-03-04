from django.db import models
from django.contrib.auth.models import AbstractUser


class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='media/users_avatars', blank=True, default='../static/img/no_avatar.png')
    age = models.PositiveIntegerField(verbose_name='возраст')
