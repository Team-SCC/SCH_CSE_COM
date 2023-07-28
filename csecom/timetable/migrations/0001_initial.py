# Generated by Django 4.2 on 2023-07-27 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grade1Timetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TextField()),
                ('MON', models.IntegerField()),
                ('TUE', models.IntegerField()),
                ('WED', models.IntegerField()),
                ('THU', models.IntegerField()),
                ('FRI', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Grade2Timetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TextField()),
                ('MON', models.IntegerField()),
                ('TUE', models.IntegerField()),
                ('WED', models.IntegerField()),
                ('THU', models.IntegerField()),
                ('FRI', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Grade3Timetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TextField()),
                ('MON', models.IntegerField()),
                ('TUE', models.IntegerField()),
                ('WED', models.IntegerField()),
                ('THU', models.IntegerField()),
                ('FRI', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Grade4Timetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TextField()),
                ('MON', models.IntegerField()),
                ('TUE', models.IntegerField()),
                ('WED', models.IntegerField()),
                ('THU', models.IntegerField()),
                ('FRI', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TimetableTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TextField()),
                ('MON', models.IntegerField()),
                ('TUE', models.IntegerField()),
                ('WED', models.IntegerField()),
                ('THU', models.IntegerField()),
                ('FRI', models.IntegerField()),
            ],
        ),
    ]