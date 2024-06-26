# Generated by Django 5.0.6 on 2024-06-05 00:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=1024)),
                ('last_name', models.CharField(max_length=1024)),
                ('specialization', models.CharField(max_length=1024)),
                ('email', models.EmailField(max_length=1024, unique=True)),
                ('phone', models.CharField(max_length=1024)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='runsomewhereapp.department')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=1024)),
                ('last_name', models.CharField(max_length=1024)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1024)),
                ('email', models.EmailField(max_length=1024, unique=True)),
                ('phone', models.CharField(max_length=1024)),
                ('address', models.TextField(max_length=1024)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('reason', models.TextField(max_length=1024)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='runsomewhereapp.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='runsomewhereapp.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medication', models.TextField(max_length=1024)),
                ('instructions', models.TextField(max_length=1024)),
                ('appointment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='runsomewhereapp.appointment')),
            ],
        ),
    ]
