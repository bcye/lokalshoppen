# Generated by Django 3.0.4 on 2020-03-21 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20200321_1330'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anfrage',
            old_name='unternehmen',
            new_name='unternehmen_id',
        ),
    ]