# Generated by Django 3.0 on 2021-07-03 03:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='Singer',
            new_name='singer',
        ),
    ]