# Generated by Django 3.1.5 on 2021-02-01 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='user_id',
            field=models.IntegerField(auto_created=1),
        ),
    ]
