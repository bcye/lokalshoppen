# Generated by Django 3.0.4 on 2020-03-29 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_auto_20200329_1204'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OberKategorie',
            new_name='Category',
        ),
        migrations.RenameModel(
            old_name='Anfrage',
            new_name='Request',
        ),
        migrations.AlterModelOptions(
            name='category',
            options={},
        ),
    ]
