# Generated by Django 3.0.4 on 2020-03-28 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_auto_20200327_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='unternehmen',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]