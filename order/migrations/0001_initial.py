# Generated by Django 3.1.5 on 2021-02-01 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.IntegerField()),
                ('specify', models.CharField(max_length=100)),
                ('user_id', models.IntegerField()),
            ],
        ),
    ]
