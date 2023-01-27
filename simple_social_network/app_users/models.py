from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.IntegerField(verbose_name='телефон', null=True, blank=True)
    city = models.CharField(max_length=30, verbose_name='город', null=True,
                            blank=True)
    subscribes_number = models.IntegerField(default=0,
                                            verbose_name='количество подписок',
                                            null=True, blank=True)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'
