# Generated by Django 5.1.2 on 2024-10-23 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CTI_APP', '0002_alter_ctilog_signature'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ctilog',
            name='owasp_category',
        ),
    ]
