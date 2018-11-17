from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class AccountUser(AbstractUser):
    avatar = models.ForeignKey(
        'images.Image',
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    phone = models.CharField(
        max_length=11,
        blank=True,
        null=True,
    )
    age = models.IntegerField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.username
