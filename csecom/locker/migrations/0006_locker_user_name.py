# Generated by Django 4.0 on 2023-07-13 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locker', '0005_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='locker',
            name='user_name',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
