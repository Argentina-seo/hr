from django.db import models


class Application(models.Model):
    name = models.CharField(max_length=255, blank=False, verbose_name='Полное имя')
    phone = models.CharField(max_length=100, blank=False, verbose_name='Телефон')
    country = models.TextChoices()
    is_samozanat = models.BooleanField(default=False, blank=False, verbose_name='Статус самозанятого')
    need_car = models.BooleanField(default=False, blank=False, verbose_name='Нужна машина?')

