from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.


class Base(models.Model):
    phone_models = models.CharField(max_length=255, verbose_name='Модель телефона')
    imei = models.IntegerField(validators=[MinValueValidator(14)],  unique=True, verbose_name='IMEI телефона')
    organization = models.CharField(max_length=255, verbose_name='Инициатор')
    num = models.IntegerField(validators=[MinValueValidator(10)], verbose_name='Номер инициатора')
    erp = models.CharField(null=True, blank=True, max_length=255, verbose_name='Номер ЕРП')
    is_active = models.BooleanField("Активный", default=True)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Добавить"
        verbose_name_plural = "Добавить данные"
        ordering = ["-created"]

    def __str__(self):
        return str(self.imei)
