# Generated by Django 5.2 on 2025-05-04 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='capital',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=45, unique=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='region',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='country',
            name='subregion',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
