# Generated by Django 3.2.5 on 2023-01-11 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_alter_member_mcarbon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='MemCity',
            field=models.CharField(default='', max_length=100, verbose_name='會員城市'),
        ),
    ]