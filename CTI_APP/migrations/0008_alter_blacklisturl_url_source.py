# Generated by Django 5.1.2 on 2024-11-21 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CTI_APP', '0007_blacklisturl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blacklisturl',
            name='url_source',
            field=models.TextField(verbose_name='URL Источника'),
        ),
    ]
