# Generated by Django 3.2.5 on 2023-01-12 23:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0024_volunteer_vchrck'),
    ]

    operations = [
        migrations.RenameField(
            model_name='volunteer',
            old_name='VChrck',
            new_name='VCheck',
        ),
    ]