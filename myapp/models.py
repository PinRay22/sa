from django.db import models
from django.utils import timezone
import datetime
from django import forms


now = timezone.now
now = datetime.datetime.now()


# 會員資料表

class member(models.Model):
    MemID = models.CharField('會員編號', max_length=1000, primary_key=True)
    MemName = models.CharField('會員姓名', max_length=20, null=False)
    MemPh = models.CharField('會員電話', max_length=50, null=False)
    MemPW = models.CharField('會員密碼', max_length=100, null=False)
    Memsanfan = models.CharField('會員身分證', max_length=100, null=False)
    MemCity = models.CharField('會員城市', max_length=100, null=False)
    MemAddr = models.CharField('會員地址', max_length=100, null=False)
    Memmail = models.CharField('會員電郵', max_length=100, null=False)
    Memxin = models.CharField('會員信用卡號', max_length=100)
    MCarbon = models.FloatField('碳排量', null=True)
    MemPoint = models.IntegerField('碳權點數', null=True)
    MemPic = models.CharField('頭貼', max_length=100, null=True)

    def __str__(self) -> str:
        return self.MemID


class order(models.Model):
    OID = models.CharField('訂單編號', max_length=1000, primary_key=True)
    Memsanfan = models.CharField('會員身分證', max_length=100, null=False)
    Serv = models.CharField('服務項目', max_length=100, null=False)
    SCarbon = models.IntegerField('碳排量', null=False)
    SPoint = models.IntegerField('消費點數', null=False)
    OCmp = models.CharField('合作廠商', max_length=100, null=False)
    SDATE = models.DateTimeField()  # 交易時間


class point(models.Model):
    PID = models.CharField('點數變更編號', max_length=1000)
    Memsanfan = models.CharField('會員身分證', max_length=100, null=False)
    PChange = models.CharField('增減', max_length=100, null=False)
    PPS = models.CharField('說明', max_length=100, null=False)
    PPoint = models.IntegerField('點數', null=False)
    PCmp = models.CharField('合作廠商', max_length=100, null=False)
    PDATE = models.DateTimeField()  # 增減時間


class Exchanged(models.Model):
    EID = models.CharField('點數兌換編號', max_length=1000)
    Memsanfan = models.CharField('會員身分證', max_length=100, null=False)
    Ename = models.CharField('服務', max_length=100, null=False)
    EPS = models.CharField('說明', max_length=100)
    EPoint = models.IntegerField('點數', null=False)
    ECmp = models.CharField('合作廠商', max_length=100, null=False)
    EDDline = models.CharField('剩餘期限', max_length=100, null=False)
    EDATE = models.DateTimeField()  # 兌換時間


class Service(models.Model):
    SID = models.CharField('服務編號', max_length=1000, primary_key=True)
    Sname = models.CharField('服務', max_length=100, null=False)
    SKind = models.CharField('服務分類', max_length=100, null=False)
    SPS = models.CharField('說明', max_length=100, null=False)
    SPoint = models.IntegerField('點數', null=False)
    SDDline = models.CharField('使用期限', max_length=100, null=False)
    SCmp = models.CharField('合作廠商', max_length=100, null=False)


class Volunteer(models.Model):
    VID = models.CharField('服務編號', max_length=1000)
    Vname = models.CharField('服務', max_length=100, null=False)
    VCarbon = models.IntegerField('碳排', null=False)
    VCmp = models.CharField('合作廠商', max_length=100)


class History(models.Model):
    HID = models.CharField('紀錄編號', max_length=1000, primary_key=True)
    Memsanfan = models.CharField('會員身分證', max_length=100, null=False)
    HDATE = models.DateTimeField()  # 交易時間
    HPS = models.CharField('說明', max_length=100, null=False)
    HPoint = models.IntegerField('點數', null=False)
    HCmp = models.CharField('合作廠商', max_length=100, null=False)
