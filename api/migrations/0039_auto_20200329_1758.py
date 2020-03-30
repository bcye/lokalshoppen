# Generated by Django 3.0.4 on 2020-03-29 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0038_auto_20200329_1700'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='business_hours_friday_end',
        ),
        migrations.RemoveField(
            model_name='company',
            name='business_hours_friday_start',
        ),
        migrations.RemoveField(
            model_name='company',
            name='business_hours_monday_end',
        ),
        migrations.RemoveField(
            model_name='company',
            name='business_hours_monday_start',
        ),
        migrations.RemoveField(
            model_name='company',
            name='business_hours_saturday_end',
        ),
        migrations.RemoveField(
            model_name='company',
            name='business_hours_saturday_start',
        ),
        migrations.RemoveField(
            model_name='company',
            name='business_hours_sunday_end',
        ),
        migrations.RemoveField(
            model_name='company',
            name='business_hours_sunday_start',
        ),
        migrations.RemoveField(
            model_name='company',
            name='business_hours_thursday_end',
        ),
        migrations.RemoveField(
            model_name='company',
            name='business_hours_thursday_start',
        ),
        migrations.RemoveField(
            model_name='company',
            name='business_hours_tuesday_end',
        ),
        migrations.RemoveField(
            model_name='company',
            name='business_hours_tuesday_start',
        ),
        migrations.RemoveField(
            model_name='company',
            name='business_hours_wednesday_end',
        ),
        migrations.RemoveField(
            model_name='company',
            name='business_hours_wednesday_start',
        ),
        migrations.CreateModel(
            name='BusinessHoursWeekday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekday', models.PositiveSmallIntegerField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')])),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Company')),
            ],
        ),
    ]