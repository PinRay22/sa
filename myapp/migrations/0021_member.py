# Generated by Django 3.2.5 on 2023-01-12 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0020_delete_member'),
    ]

    operations = [
        migrations.CreateModel(
            name='member',
            fields=[
                ('MemID', models.CharField(max_length=1000, primary_key=True, serialize=False, verbose_name='會員編號')),
                ('MemName', models.CharField(max_length=20, verbose_name='會員姓名')),
                ('MemPh', models.CharField(max_length=50, verbose_name='會員電話')),
                ('MemPW', models.CharField(max_length=100, verbose_name='會員密碼')),
                ('Memsanfan', models.CharField(max_length=100, verbose_name='會員身分證')),
                ('MemCity', models.CharField(max_length=100, verbose_name='會員城市')),
                ('MemAddr', models.CharField(max_length=100, verbose_name='會員地址')),
                ('Memmail', models.CharField(max_length=100, verbose_name='會員電郵')),
                ('Memxin', models.CharField(max_length=100, verbose_name='會員信用卡號')),
                ('MCarbon', models.FloatField(null=True, verbose_name='碳排量')),
                ('MemPoint', models.IntegerField(null=True, verbose_name='碳權點數')),
                ('MemPic', models.CharField(max_length=100, null=True, verbose_name='頭貼')),
            ],
        ),
    ]
