# Generated by Django 4.2.15 on 2024-12-07 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocm', '0002_rename_first_name_student_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfficeHour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of_week', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday')], max_length=9)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
    ]
