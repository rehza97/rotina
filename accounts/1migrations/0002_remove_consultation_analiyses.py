# Generated by Django 5.0.6 on 2024-06-04 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consultation',
            name='analiyses',
        ),
    ]
