# Generated by Django 3.0.4 on 2020-03-29 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0031_auto_20200329_1213'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='telefon',
            new_name='phone',
        ),
        migrations.RenameField(
            model_name='request',
            old_name='kunden_email',
            new_name='customer_email',
        ),
    ]
