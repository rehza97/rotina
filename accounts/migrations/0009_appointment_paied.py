# Generated by Django 5.0.6 on 2024-06-03 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_remove_appointment_paied_paymenets'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='paied',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
