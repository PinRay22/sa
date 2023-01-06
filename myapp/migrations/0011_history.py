# Generated by Django 3.2.5 on 2023-01-05 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_service_sddline'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('HID', models.CharField(max_length=1000, primary_key=True, serialize=False, verbose_name='紀錄編號')),
                ('Memsanfan', models.CharField(max_length=100, verbose_name='會員身分證')),
                ('HDATE', models.DateTimeField()),
                ('HPS', models.CharField(max_length=100, verbose_name='說明')),
                ('HPoint', models.IntegerField(verbose_name='點數')),
                ('HCmp', models.CharField(max_length=100, verbose_name='合作廠商')),
            ],
        ),
    ]
