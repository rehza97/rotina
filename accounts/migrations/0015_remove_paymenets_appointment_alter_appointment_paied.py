# Generated by Django 5.0.6 on 2024-06-03 23:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_paymenets_appointment_alter_appointment_paied'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymenets',
            name='appointment',
        ),
        migrations.AlterField(
            model_name='appointment',
            name='paied',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.paymenets'),
        ),
    ]