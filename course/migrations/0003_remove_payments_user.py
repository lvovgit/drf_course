# Generated by Django 4.2.2 on 2023-07-12 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_payments_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payments',
            name='user',
        ),
    ]
