from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.db.models import Count
from django.contrib import auth, messages
from datetime import datetime, timezone, timedelta
from myapp.models import *
from django.contrib.auth.models import User
from systemanalyst import settings
from django.template.loader import render_to_string
from django.contrib.sessions.models import Session
from jinja2 import Environment, FileSystemLoader
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

#timmmme
now = timezone.now
now = datetime.datetime.now()


#email初始格式
content = MIMEMultipart()  #建立MIMEMultipart物件
content["subject"] = "您的碳制郎安全密碼驗證"  #郵件標題
content["from"] = "pydemo123@gmail.com"  #寄件者
content["to"] = "hatori1129ckmia@gmail.com" #收件者
content.attach(MIMEText("請使用密碼以驗證簽署者身份\n\n   您必須在十分鐘內輸入以下安全密碼，\n   以簽署由碳制郎股份有限公司發送給您的。\n\t\t您的驗證碼： 852 416 \n   你沒有提出申請嗎？\n   若你並未提出此申請，請忽略此信。若重複收到此信，請注意帳號安全或聯絡客服人員。\n   有任何疑問請聯絡客服，當然也歡迎你註冊專屬自己的碳制郎帳號！\n" ))  #郵件內容

def send_email():
    with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器
        try:
            smtp.ehlo()  # 驗證SMTP伺服器
            smtp.starttls()  # 建立加密傳輸
            smtp.login("pinray544513@gmail.com", "cqjmnljocygiqqvk")  # 登入寄件者gmail
            smtp.send_message(content)  # 寄送郵件
            print("Complete!")
        except Exception as e:
            print("Error message: ", e)

def insert(request):
    order.MemID = 1
    order.Memsanfan = 1
    order.Serv = '洗衣服'
    order.SCarbon = 666
    order.SPoint = 10
    order.SDATE = 2023/1/6
    order.save()
    return render(request, 'index.html', locals())


def start(request):
    return render(request, 'before_login.html', locals())


def pe_view(request):
    sname = request.POST.get('name', '')
    ser = Service.objects.get(Sname=sname)
    return render(request, 'point_exc.html', locals())
    
def use_view(request):
    sname = request.POST.get('dname', '')
    eer = Exchanged.objects.get( Ename = sname )
    return render(request, 'point_use.html', locals())

def acti_p(request):
    san = request.session.get('session_id')
    if san != 0 and san is not None:
        item = Volunteer.objects.get()
        cd = item.VCarbon
        user = member.objects.get(Memsanfan=san)
        mcd = user.MCarbon
        member.objects.filter(Memsanfan=san).update(MCarbon=(mcd - cd))
        messages.error(request, '太棒了!一起為地球努力吧')
        return HttpResponseRedirect("/point_view/")
    else:
        messages.error(request, '您尚未登入，請先登入')
        return HttpResponseRedirect("/login/")


def point_view(request):
    san = request.session.get('session_id')
    if san != 0 and san is not None:
        item = member.objects.get(Memsanfan=san)
        users = point.objects.filter(Memsanfan=san)
        ser1 = Service.objects.filter(SKind=1)
        ser2 = Service.objects.filter(SKind=2)
        ser3 = Service.objects.filter(SKind=3)
        ser4 = Service.objects.filter(SKind=4)
        ser5 = Service.objects.filter(SKind=5)
        exs = Exchanged.objects.filter(Memsanfan=san)
        return render(request, 'point.html', locals())
    else:
        messages.error(request, '您尚未登入，請先登入')
        return HttpResponseRedirect("/login/")


def record_view(request):
    san = request.session.get('session_id')
    if san != 0 and san is not None:
        items = order.objects.filter(Memsanfan=san)
        # user = .objects.get(PHONE_NUMBER = user_phone)
        #user_point = user.POINT
        return render(request, 'record.html', locals())
    else:
        messages.error(request, '您尚未登入，請先登入')
        return HttpResponseRedirect("/login/")


def cmphoto(request):
    san = request.session.get('session_id')
    Pic = request.POST.get('picnum', '')
    member.objects.filter(Memsanfan=san).update(MemPic=Pic)
    messages.error(request, '完成頭貼更換')
    return HttpResponseRedirect("/vmember/")


def rede(request):
    cmp = request.POST.get('Cname', '')
    user = order.objects.get(OCmp=cmp)
    return render(request, 'record_detail.html', locals())


def index(request):
    san = request.session.get('session_id')
    print(san)
    items = Volunteer.objects.all()
    user = member.objects.get(Memsanfan=san)
    cks = Volunteer.objects.all()
    
    return render(request, 'index.html', locals())


def login_view(request):
    return render(request, 'login.html', locals())

#任務畫面
def activity_view(request):
    items = Volunteer.objects.all()
    return render(request, 'activity.html', locals())

#開始任務
def in_progress_view(request):
    name = request.POST.get('vname', '')
    items = Volunteer.objects.filter( Vname = name )
    return render(request, 'in_progress.html', locals())

#確認任務
def check_mission(request):
    name = request.POST.get('vname', '')
    Volunteer.objects.filter( Vname = name ).update( VCheck = True )
    print("adadadadadadadadad")
    return HttpResponseRedirect("/index/")

def vmem_photo(request):
    return render(request, 'mem_photo.html', locals())

def rank(request):
    san = request.session.get('session_id')
    user = member.objects.get(Memsanfan=san)
    Mem_city = user.MemCity
    Mem_CB = user.MCarbon
    Mem_name = user.MemName
    fcity = request.POST.get('inputCity', '')
    if fcity is not None :
        mydata = member.objects.filter( MemCity = fcity ).order_by('MCarbon').values()
        return render(request, 'rank.html', locals())
    else :
        messages.error(request, '查無資料喔')
        return HttpResponseRedirect("/rank/")

def rank_view(request):
    san = request.session.get('session_id')
    print(san)
    user = member.objects.get( Memsanfan = san )
    if san != 0 and san is not None:
        Mem_city = user.MemCity
        Mem_CB = user.MCarbon
        Mem_name = user.MemName
        mydata = member.objects.filter( MemCity = Mem_city ).order_by('MCarbon').values()
        return render(request, 'rank.html', locals())
    else:
        messages.error(request, '您尚未登入，請先登入')
        return HttpResponseRedirect("/login/")

def comp_view(request):
    san = request.session.get('session_id')
    if san != 0 and san is not None:
        return render(request, 'comp.html', locals())
    else:
        messages.error(request, '您尚未登入，請先登入')
        return HttpResponseRedirect("/login/")


def logout(request):
    request.session['session_id'] = 0
    messages.error(request, '你登出囉')
    # return render(request, 'index.html', locals())
    return HttpResponseRedirect("/indexf/")


def delete(request):
    san = request.session.get('session_id')
    sname = request.POST.get('eerName', '')
    dd = Exchanged.objects.get( Ename = sname )
    dd.delete()
    ss = Service.objects.get( Sname = sname )
    car =ss.SCarbon
    user = member.objects.get(Memsanfan=san)
    user.MCarbon = user.MCarbon + car
    user.save()
    messages.error(request, '用爽沒')
    return HttpResponseRedirect("/point_view/")


def exchange(request):
    san = request.session.get('session_id')
    print(san)
    sname = request.POST.get('SerName', '')
    user = member.objects.get(Memsanfan=san)
    Mpoint = user.MemPoint
    #Sername = str(request.POST.get('SerName'))
    Ser = Service.objects.get(Sname=sname)
    ddate = int(Ser.SDDline) - 1
    PointCost = Ser.SPoint
    Scar = Ser.SCarbon
    if Mpoint < PointCost:
        messages.error(request, '您的點數需大於兌換點數！')
        return HttpResponseRedirect("/point_view/")
    member.objects.filter(Memsanfan=san).update(MemPoint=(Mpoint - PointCost))
    pp = point(PID='0', Memsanfan=san, PChange='-', PPS=sname, PCarbon = Scar,
               PPoint=PointCost, PCmp='0', PDATE=now, )
    pp.save()
    ee = Exchanged(EID='0', Memsanfan=san, Ename=sname, ECarbon = Scar,
                   EPoint=PointCost, ECmp='0', EDDline=ddate, EDATE=now)
    ee.save()
    messages.error(request, '兌換成功')
    return HttpResponseRedirect("/point_view/")

def submit(request):
    request.post('https://33ea-61-63-97-78.jp.ngrok.io/SA/test.jsp', data = {
        "objectId": "1",
        "objectType": "1",
        "objectUseable": "智慧你",
        "objectOwner": 10,
    })
    return render(request, 'index.html', locals())

#碳排增減    
def changecb(request):
    san = request.session.get('session_id')
    user = member.objects.get(Memsanfan=san)
    if request.method == 'POST':
        form = request.POST
        plus = form['plusnum']
        minus = form['minusnum']
        memCarbon = user.MCarbon
        
        member.objects.filter(Memsanfan=san).update(MCarbon=(memCarbon - float(minus)+ float(plus)))
        messages.error(request, '修改成功')
        return render(request, 'activity.html', locals())

def member_view(request):
    san = request.session.get('session_id')
    print(san)
    user = member.objects.get(Memsanfan=san)
    if user is not None and san != 0:
        Mem_sanfan = user.Memsanfan
        Mem_name = user.MemName
        Mem_phone = user.MemPh
        Mem_password = user.MemPW
        Mem_city = user.MemCity
        Mem_address = user.MemAddr
        Mem_mail = user.Memmail
        Mem_xin = user.Memxin
        Mem_point = user.MemPoint
        Mem_pic = user.MemPic
        Mem_CB = user.MCarbon
        return render(request, 'vmember.html', locals())
    else:
        messages.error(request, '您尚未登入，請先登入')
        return HttpResponseRedirect("/login/")


def login_p(request):
    sanfan = request.POST.get('san', '')
    password = request.POST.get('password', '') 
    m = member.objects.filter( Memsanfan = sanfan )
    if m:
        b = member.objects.get( Memsanfan = sanfan )
        if b.Memsanfan == sanfan and b.MemPW == password:
            request.session['session_id'] = sanfan
            print(request.session['session_id']) # 設置session
            s = Session.objects.all()
            print(sanfan)
            messages.error(request, '登入成功')
            return HttpResponseRedirect("/index/")
        #return render(request, '/index/', locals())
        else :
            request.session['session_id'] = 0
            messages.error(request, '密碼錯誤')  
            return HttpResponseRedirect("/login/")
            #return render(request, '/login/', locals())
    else :
        request.session['session_id'] = 0
        messages.error(request, '查無帳號資訊')  
        return HttpResponseRedirect("/login/")


def signup_view(request):
    return render(request, 'signup.html', locals())


def alt_view(request):
    san = request.session.get('session_id')
    print(san)
    user = member.objects.get(Memsanfan=san)
    Mem_sanfan = user.Memsanfan
    Mem_name = user.MemName
    Mem_phone = user.MemPh
    Mem_password = user.MemPW
    Mem_city = user.MemCity
    Mem_address = user.MemAddr
    Mem_mail = user.Memmail
    Mem_xin = user.Memxin
    Mem_point = user.MemPoint
    return render(request, 'alt_member.html', locals())



def alt_member(request):
    memsan = request.session.get('session_id')
    if request.method == 'POST':
        form = request.POST
        tName = form['name']
        tPh = form['phone']
        tPW = form['password']
        tCity = form['city']
        tAddr = form['address']
        tmail = form['mail']
        txin = form['xin']
        user = member.objects.get(Memsanfan=memsan)
        if user is not None and memsan != 0:
            user.MemName = tName
            user.MemPh = tPh
            user.MemPW = tPW
            user.Memmail = tmail
            user.MemCity = tCity
            user.MemAddr = tAddr
            user.Memxin = txin
            user.save()
            print("success")
            messages.error(request, '修改成功')
            return redirect('/vmember/')
    else:
        messages.error(request, '修改失敗')
        return redirect('/alt_view/')


def signup(request):
    if request.method == 'POST':
        form = request.POST
        tMemID = form['san']
        tMemName = form['name']
        tMemPh = form['phone']
        tMemPW = form['password']
        tMemsanfan = form['san']
        tMemCity = form['city']
        tMemAddr = form['address']
        tMemmail = form['mail']
        tMemxin = form['xin']
        newmember = member(MemID=tMemID,
                           MemName=tMemName, MemPh=tMemPh,
                           MemPW=tMemPW, Memsanfan=tMemsanfan, MemCity=tMemCity,
                           MemAddr=tMemAddr, Memmail=tMemmail,
                           Memxin=tMemxin, MCarbon=0, MemPoint=0, MemPic='../static/img/mem_pic1.jpg')
        newmember.save()
        print("success")
        messages.error(request, '註冊成功')
        return HttpResponseRedirect("/login/")  # 要改  /index#loginModal/沒屁用
    else:
        messages.error(request, '註冊失敗')
        return HttpResponseRedirect('/signup_view/')
# def incre():
#    qs = member.objects.all()
#    last_obj = qs.latest('tMemID')
#    tMemID = '{0:03d}'.format(int(last_obj.tMemID) + 1)
#    return tMemID

# def signin(request):
    if request.method == 'POST':
        form = request.POST
        tMemsanfan = form['san']
        tMemPW = form['password']

        try:
            unit = member.objects.get(Memsanfan=tMemsanfan)
            if unit.Memsanfan == tMemsanfan and unit.MemPW == tMemPW:
                global ck
                ck = tMemsanfan
                print(ck)
                # return redirect('/index/')
                win32api.MessageBox(0, 'success', 'login')
                return render(request, "index.html", locals())
            else:
                # return redirect('/index/')
                return Server.Transfer("/index#loginModal/")

        except:
            errormessage = "error"

        return redirect('/index/')  # 要改  /index#loginModal/沒屁用
    else:
        return render(request, '/index/')
