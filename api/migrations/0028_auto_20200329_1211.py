# Generated by Django 3.0.4 on 2020-03-29 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0027_auto_20200329_1210'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='adresse',
            new_name='address',
        ),
    ]
