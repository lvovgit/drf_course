# Generated by Django 4.2.2 on 2023-07-24 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, choices=[('member', 'member'), ('moderator', 'moderator')], default='member', max_length=10, null=True, verbose_name='роль'),
        ),
    ]
