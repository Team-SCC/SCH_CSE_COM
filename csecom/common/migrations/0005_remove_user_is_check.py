# Generated by Django 4.2 on 2023-06-20 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_user_is_check'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_check',
        ),
    ]