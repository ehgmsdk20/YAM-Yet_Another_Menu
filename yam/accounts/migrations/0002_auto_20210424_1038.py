# Generated by Django 3.2 on 2021-04-24 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='home_latlng',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='profile',
            name='office_latlng',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]