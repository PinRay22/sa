# Generated by Django 3.2.5 on 2023-01-13 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0025_rename_vchrck_volunteer_vcheck'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='Memrank',
            field=models.IntegerField(default=1, verbose_name='徽章'),
            preserve_default=False,
        ),
    ]