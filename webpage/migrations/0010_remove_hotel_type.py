# Generated by Django 3.0.4 on 2020-05-20 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0009_hotel_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='type',
        ),
    ]
