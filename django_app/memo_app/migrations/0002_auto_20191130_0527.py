# Generated by Django 2.2.7 on 2019-11-30 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('memo_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='memo',
            old_name='update_datefile',
            new_name='update_datetime',
        ),
    ]
