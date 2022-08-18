# Generated by Django 3.2.12 on 2022-03-29 06:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=20, null=True)),
                ('last_name', models.CharField(blank=True, max_length=20, null=True)),
                ('phone', models.CharField(blank=True, max_length=10, null=True)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LeaveRequest',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('request_date', models.DateField(blank=True, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('leave_date_details', models.JSONField(blank=True, default=dict, null=True)),
                ('total', models.FloatField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('APPROVED', 'APPROVED'), ('PENDING', 'PENDING'), ('REJECTED', 'REJECTED'), ('CANCELLED', 'CANCELLED')], default='PENDING', max_length=20, null=True)),
                ('reason', models.CharField(blank=True, max_length=200, null=True)),
                ('comments', models.JSONField(blank=True, default=dict, null=True)),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.employee')),
            ],
        ),
    ]