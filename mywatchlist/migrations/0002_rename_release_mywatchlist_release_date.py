# Generated by Django 4.1 on 2022-09-17 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mywatchlist', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mywatchlist',
            old_name='release',
            new_name='release_date',
        ),
    ]
