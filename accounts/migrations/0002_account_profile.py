# Generated by Django 5.0.6 on 2024-06-01 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='profile',
            field=models.BooleanField(default=False),
        ),
    ]
