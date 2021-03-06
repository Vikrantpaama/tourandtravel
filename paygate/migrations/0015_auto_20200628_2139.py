# Generated by Django 3.0.4 on 2020-06-28 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paygate', '0014_auto_20200613_2157'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='State',
            new_name='gender',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='City',
            new_name='packagename',
        ),
        migrations.RemoveField(
            model_name='book',
            name='Address',
        ),
        migrations.RemoveField(
            model_name='book',
            name='Address2',
        ),
        migrations.RemoveField(
            model_name='book',
            name='check_in_date',
        ),
        migrations.RemoveField(
            model_name='book',
            name='check_out_date',
        ),
        migrations.AddField(
            model_name='book',
            name='amount',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
