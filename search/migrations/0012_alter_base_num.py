# Generated by Django 3.2.9 on 2022-02-24 16:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0011_auto_20220224_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='base',
            name='num',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(10)], verbose_name='Номер инициатора'),
        ),
    ]