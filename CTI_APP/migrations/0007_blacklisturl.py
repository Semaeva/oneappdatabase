# Generated by Django 5.1.2 on 2024-11-21 11:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CTI_APP', '0006_blacklistip_remove_ctilog_attack_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlackListURL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_source', models.GenericIPAddressField(verbose_name='IP Источника')),
                ('attack_date', models.IntegerField(help_text='Введите год, когда была обнаружена вредносная ПО', validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2024)], verbose_name='Год появления URL')),
            ],
            options={
                'verbose_name': 'Black List URL',
                'verbose_name_plural': 'Black List URL',
            },
        ),
    ]
