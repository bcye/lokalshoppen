# Generated by Django 3.0.4 on 2020-03-29 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0032_auto_20200329_1217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='categories',
        ),
        migrations.AddField(
            model_name='company',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Category'),
        ),
    ]
