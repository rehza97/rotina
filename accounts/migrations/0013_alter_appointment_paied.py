# Generated by Django 5.0.6 on 2024-06-03 23:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_remove_paymenets_appointment_alter_appointment_paied'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='paied',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.paymenets'),
        ),
    ]
