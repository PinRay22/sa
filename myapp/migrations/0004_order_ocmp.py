# Generated by Django 3.2.5 on 2023-01-05 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20230106_0159'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='OCmp',
            field=models.CharField(default=1, max_length=100, verbose_name='合作廠商'),
            preserve_default=False,
        ),
    ]
