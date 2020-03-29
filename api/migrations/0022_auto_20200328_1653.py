# Generated by Django 3.0.4 on 2020-03-28 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_auto_20200328_1616'),
    ]

    operations = [
        migrations.CreateModel(
            name='OberKategorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=3)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UnterKategorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Kategorien',
        ),
        migrations.RemoveField(
            model_name='unternehmen',
            name='ober_kategorie',
        ),
        migrations.RemoveField(
            model_name='unternehmen',
            name='unter_kategorien',
        ),
        migrations.AddField(
            model_name='unternehmen',
            name='ober_kategorien',
            field=models.ManyToManyField(to='api.OberKategorie'),
        ),
        migrations.AddField(
            model_name='unternehmen',
            name='unter_kategorien',
            field=models.ManyToManyField(to='api.UnterKategorie'),
        ),
    ]