# Generated by Django 3.1.7 on 2021-03-31 11:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210331_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mobileNo',
            field=models.CharField(max_length=15, unique=True, validators=[django.core.validators.RegexValidator(message='Phone number must be entered in the format 9999999999. Only 10 digits allowed.', regex='^\\+?1?\\d{10}$')]),
        ),
    ]
