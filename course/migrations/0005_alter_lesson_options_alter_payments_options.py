# Generated by Django 4.2.2 on 2023-07-18 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_payments_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lesson',
            options={'ordering': ('name',), 'verbose_name': 'Урок', 'verbose_name_plural': 'Уроки'},
        ),
        migrations.AlterModelOptions(
            name='payments',
            options={'ordering': ('payment_date',), 'verbose_name': 'Платеж', 'verbose_name_plural': 'Платежи'},
        ),
    ]
