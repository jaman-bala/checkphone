# Generated by Django 3.2.9 on 2022-02-24 16:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0006_alter_base_imei'),
    ]

    operations = [
        migrations.AlterField(
            model_name='base',
            name='num',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(9), django.core.validators.MaxValueValidator(11)], verbose_name='Номер инициатора'),
        ),
    ]
