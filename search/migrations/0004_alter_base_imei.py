# Generated by Django 3.2.9 on 2022-02-24 13:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0003_alter_base_imei'),
    ]

    operations = [
        migrations.AlterField(
            model_name='base',
            name='imei',
            field=models.IntegerField(unique=True, validators=[django.core.validators.MinValueValidator(14), django.core.validators.MaxValueValidator(15)], verbose_name='IMEI телефона'),
        ),
    ]
