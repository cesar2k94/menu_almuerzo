# Generated by Django 3.1.5 on 2021-02-09 20:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0013_auto_20210202_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
