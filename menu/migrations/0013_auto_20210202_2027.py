# Generated by Django 3.1.5 on 2021-02-02 23:27

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0012_auto_20210131_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='date',
            field=models.DateField(validators=[django.core.validators.MinValueValidator(limit_value=datetime.date.today)]),
        ),
    ]
