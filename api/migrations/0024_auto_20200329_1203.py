# Generated by Django 3.0.4 on 2020-03-29 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_auto_20200329_0911'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Unternehmen',
            new_name='Company',
        ),
        migrations.AlterModelOptions(
            name='company',
            options={},
        ),
    ]