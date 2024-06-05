# Generated by Django 5.0.6 on 2024-05-29 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('runsomewhereapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='reason',
            field=models.TextField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='email',
            field=models.EmailField(max_length=1024, unique=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='first_name',
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='last_name',
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='phone',
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='specialization',
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='patient',
            name='address',
            field=models.TextField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='patient',
            name='email',
            field=models.EmailField(max_length=1024, unique=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='first_name',
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1024),
        ),
        migrations.AlterField(
            model_name='patient',
            name='last_name',
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone',
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='instructions',
            field=models.TextField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='medication',
            field=models.TextField(max_length=1024),
        ),
    ]