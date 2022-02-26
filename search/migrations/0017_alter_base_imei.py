# Generated by Django 3.2.9 on 2022-02-24 17:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0016_alter_base_imei'),
    ]

    operations = [
        migrations.AlterField(
            model_name='base',
            name='imei',
            field=models.IntegerField(unique=True, validators=[django.core.validators.MinValueValidator(13), django.core.validators.MaxValueValidator(14)], verbose_name='IMEI телефона'),
        ),
    ]
