# Generated by Django 5.1.2 on 2024-10-23 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CTI_APP', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ctilog',
            name='signature',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Сигнатура'),
        ),
    ]
