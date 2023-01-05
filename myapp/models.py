from django.db import models
from django.utils import timezone
import datetime
from django import forms



now = timezone.now
now = datetime.datetime.now()


#會員資料表

class member(models.Model):
    MemID = models.CharField('會員編號',max_length=1000,primary_key=True)
    MemName = models.CharField('會員姓名', max_length=20, null=False)
    MemPh = models.CharField('會員電話', max_length=50, null=False)
    MemPW = models.CharField('會員密碼', max_length=100, null=False)
    Memsanfan = models.CharField('會員身分證', max_length=100, null=False)
    MemAddr = models.CharField('會員地址', max_length=100, null=False)
    Memmail = models.CharField('會員電郵', max_length=100, null=False)
    Memxin = models.CharField('會員信用卡號', max_length=100, null=False)
    MemPoint = models.IntegerField('碳權點數', null=True)

    def __str__(self) -> str:
        return self.MemID

