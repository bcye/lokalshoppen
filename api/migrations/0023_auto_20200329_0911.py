# Generated by Django 3.0.4 on 2020-03-29 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_auto_20200328_1653'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='anfrage',
            options={'verbose_name': 'Anfrage', 'verbose_name_plural': 'Anfragen'},
        ),
        migrations.AlterModelOptions(
            name='oberkategorie',
            options={'verbose_name': 'Oberkategorie', 'verbose_name_plural': 'Oberkategorien'},
        ),
        migrations.AlterModelOptions(
            name='unterkategorie',
            options={'verbose_name': 'Unterkategorie', 'verbose_name_plural': 'Unterkategorien'},
        ),
        migrations.AlterModelOptions(
            name='unternehmen',
            options={'verbose_name': 'Unternehmen', 'verbose_name_plural': 'Unternehmen'},
        ),
        migrations.RemoveField(
            model_name='timeslot',
            name='count',
        ),
    ]
