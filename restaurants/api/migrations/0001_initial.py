# Generated by Django 3.0 on 2021-06-25 15:31

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurants',
            fields=[
                ('id', models.UUIDField(default=True, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=120, unique=True, verbose_name='Name')),
                ('direction', models.CharField(max_length=120, verbose_name='Direction')),
                ('phone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=120, unique=True, verbose_name='Name')),
                ('type', models.CharField(choices=[('BREAKFAST', 'Breakfast'), ('LUNCH', 'Lunch'), ('COFFEE', 'Coffee'), ('DINNER', 'Dinner')], max_length=20)),
                ('thumbnail', models.ImageField(default='recipe_thumbnails/default.png', upload_to='recipe_thumbnails')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Restaurants')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=120, unique=True, verbose_name='Name')),
                ('recipe', models.ManyToManyField(to='api.Recipe')),
            ],
        ),
    ]
