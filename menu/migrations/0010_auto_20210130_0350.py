# Generated by Django 3.1.5 on 2021-01-30 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0009_auto_20210130_0349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='date',
            field=models.DateField(),
        ),
    ]
