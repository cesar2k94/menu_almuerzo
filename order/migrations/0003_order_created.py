# Generated by Django 3.1.5 on 2021-02-02 23:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20210201_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='created',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
