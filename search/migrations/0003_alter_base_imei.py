# Generated by Django 3.2.9 on 2022-02-24 13:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_auto_20220224_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='base',
            name='imei',
            field=models.IntegerField(default=0, unique=True, validators=[django.core.validators.MinValueValidator(14), django.core.validators.MaxValueValidator(15)], verbose_name='IMEI телефона'),
        ),
    ]
