# Generated by Django 3.0.4 on 2020-06-12 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paygate', '0012_auto_20200612_2057'),
    ]

    operations = [
        migrations.RenameField(
            model_name='airbook',
            old_name='Bussiness',
            new_name='class1',
        ),
        migrations.RenameField(
            model_name='airbook',
            old_name='One_Way',
            new_name='trip_type',
        ),
        migrations.RemoveField(
            model_name='airbook',
            name='First',
        ),
        migrations.RemoveField(
            model_name='airbook',
            name='Premium_Economy',
        ),
        migrations.RemoveField(
            model_name='airbook',
            name='Round_Trip',
        ),
        migrations.RemoveField(
            model_name='airbook',
            name='economy',
        ),
    ]
