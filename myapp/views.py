from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.db.models import Count
from django.contrib import auth,messages
from datetime import datetime,timezone,timedelta
from myapp.models import *
from django.contrib.auth.models import User
from systemanalyst import settings
from django.template.loader import render_to_string
from django.contrib.sessions.models import Session
from jinja2 import Environment, FileSystemLoader


def insert(request):
    order.MemID = 1
    order.Memsanfan = 1
    order.Serv = '洗衣服'
    order.SCarbon = 666
    order.SPoint = 10
    order.SDATE = 2023/1/6
    order.save()
    return render(request, 'index.html', locals())

def point_view(request):
    san=request.session.get('session_id')
    if san != 0 and san is not None :
        item = member.objects.get( Memsanfan = san )
        users = point.objects.filter( Memsanfan = san )
        ser1 = Service.objects.filter( SKind = 1 )
        ser2 = Service.objects.filter( SKind = 2 )
        ser3 = Service.objects.filter( SKind = 3 )
        ser4 = Service.objects.filter( SKind = 4 )
        ser5 = Service.objects.filter( SKind = 5 )
        exs = Exchanged.objects.filter( Memsanfan = san )
        return render(request, 'point.html', locals())
    else:
        messages.error(request, '您尚未登入，請先登入')
        return HttpResponseRedirect("/login/")
    

def record_view(request):
    san=request.session.get('session_id')
    if san != 0 and san is not None :
        items = order.objects.filter( Memsanfan = san )
        #user = .objects.get(PHONE_NUMBER = user_phone)
        #user_point = user.POINT
        return render(request, 'record.html', locals())
    else:
        messages.error(request, '您尚未登入，請先登入')
        return HttpResponseRedirect("/login/")


def index(request): 
    san=request.session.get('session_id')
    print(san)
    return render(request, 'index.html', locals())

def login_view(request):
    return render(request, 'login.html', locals())

def rank_view(request):
    return render(request, 'rank.html', locals())

def comp_view(request):
    return render(request, 'comp.html', locals())

def logout(request): 
    request.session['session_id'] = 0
    messages.error(request, '你登出囉')  
    #return render(request, 'index.html', locals())
    return HttpResponseRedirect("/index/")

def exchange(request):
    san=request.session.get('session_id')
    user = member.objects.get( Memsanfan = san )
    point = user.MemPoint
    SerName = request.POST.get("ser_name")
    Ser = Exchanged.objects.get( Ename = SerName )
    PointCost = Ser.EPoint 
    if point < PointCost :
        messages.error(request, '您的點數需大於兌換點數！')
        return HttpResponseRedirect("/exchange/")
    member.objects.filter( Memsanfan = san ).update( MemPoint = ( point - PointCost))
    messages.error(request, '兌換成功')
    return HttpResponseRedirect("/exchange/")
    

def member_view(request):
    san=request.session.get('session_id')
    print(san)
    user = member.objects.get( Memsanfan = san )
    if user is not None and san != 0 :
        Mem_sanfan = user.Memsanfan
        Mem_name=user.MemName
        Mem_phone=user.MemPh
        Mem_password=user.MemPW
        Mem_address=user.MemAddr
        Mem_mail=user.Memmail
        Mem_xin=user.Memxin
        Mem_point=user.MemPoint
        return render(request, 'vmember.html', locals())
    else:
        messages.error(request, '您尚未登入，請先登入')
        return HttpResponseRedirect("/login/")

def login_p(request):
    sanfan = request.POST.get('san', '')
    password = request.POST.get('password', '') 
    m = member.objects.get( Memsanfan = sanfan )
    if m.Memsanfan == sanfan and m.MemPW == password:
        request.session['session_id'] = sanfan
        print(request.session['session_id']) # 設置session
        s = Session.objects.all()
        print(sanfan)
        messages.error(request, '登入成功')
        return render(request, 'index.html', locals())
    else :
        request.session['session_id'] = 0
        messages.error(request, '帳號或密碼錯誤')  
        return render(request, 'login.html', locals())
   


""" def login_p(request):
    if request.user.is_authenticated:
        print("is auth")
        return HttpResponseRedirect('/index/')
    ck = member.objects.filter( Memsanfan = request.POST['san']).count()
    print("ck",ck)
    if ck == 0 :
        messages.error(request, '帳號或密碼錯誤')  
        return render(request, 'index.html', locals())
    m = member.objects.get( Memsanfan = request.POST['san'])
    if m.MemPW != request.POST['password']:
        messages.error(request, '帳號或密碼錯誤')  
        return render(request, 'index.html', locals())
    username = request.POST.get('san', '')
    password = request.POST.get('password', '')
    user = auth.authenticate( username = username, password = password)
    if user is not None and user.is_active:
        print(user)
        print('user.is_active')
        auth.login(request, user)
        messages.error(request, '登入成功')  
        return render(request, 'index.html', locals())
    else:
        print(user)
        print('user.n_active')
        return render(request, 'index.html', locals()) """

def main(request):
    if request.user.is_authenticated:
        san = request.user
        user = member.objects.get( Memsanfan = san )
        Mem_name=member.MemName
        Mem_phone=member.MemPh
        Mem_password=member.MemPW
        Mem_address=member.MemAddr
        Mem_mail=member.Memmail
        Mem_xin=member.Memxin
        Mem_point=member.MemPoint
    return render(request, 'index.html', locals())

def signup_view(request):
    return render(request, 'signup.html', locals())

def alt_view(request):
    san=request.session.get('session_id')
    print(san)
    user = member.objects.get( Memsanfan = san )
    Mem_sanfan = user.Memsanfan
    Mem_name=user.MemName
    Mem_phone=user.MemPh
    Mem_password=user.MemPW
    Mem_address=user.MemAddr
    Mem_mail=user.Memmail
    Mem_xin=user.Memxin
    Mem_point=user.MemPoint
    return render(request, 'alt_member.html', locals())

def alt_member(request):
    memsan=request.session.get('session_id')
    if request.method == 'POST':
        form = request.POST
        tName=form['name']
        tPh = form['phone']
        tPW = form['password']
        tAddr = form['address']
        tmail = form['mail']
        txin = form['xin']
        user = member.objects.get( Memsanfan = memsan )
        if user is not None and memsan != 0 :
            user.MemName  = tName
            user.MemPh = tPh
            user.MemPW = tPW
            user.Memmail = tmail
            user.MemAddr = tAddr
            user.Memxin = txin
            user.save()
            print("success")
            messages.error(request, '修改成功')
            return redirect('/index/') 
    else:
        messages.error(request, '修改失敗')
        return redirect('/alt_view/')

def signup(request):
    if request.method == 'POST':
        form = request.POST
        tMemID=form['name']
        tMemName=form['name']
        tMemPh = form['phone']
        tMemPW = form['password']
        tMemsanfan = form['san']
        tMemAddr = form['address']
        tMemmail = form['mail']
        tMemxin = form['xin']
        newmember = member( MemID = tMemID, MemName = tMemName, MemPh = tMemPh, MemPW= tMemPW, Memsanfan = tMemsanfan, MemAddr = tMemAddr, Memmail = tMemmail, Memxin = tMemxin)
        newmember.save()
        print("success")
        messages.error(request, '註冊成功')
        return redirect('/index/') #要改  /index#loginModal/沒屁用
    else:
        messages.error(request, '註冊失敗')
        return redirect('/signup_view/')
#def incre():
#    qs = member.objects.all()
#    last_obj = qs.latest('tMemID')
#    tMemID = '{0:03d}'.format(int(last_obj.tMemID) + 1)
#    return tMemID

#def signin(request):
    if request.method == 'POST':
        form = request.POST
        tMemsanfan = form['san']
        tMemPW = form['password']
        
        try:
            unit = member.objects.get(Memsanfan = tMemsanfan)
            if unit.Memsanfan == tMemsanfan and unit.MemPW == tMemPW :
                global ck
                ck = tMemsanfan
                print(ck)
                #return redirect('/index/')
                win32api.MessageBox(0, 'success', 'login')
                return render(request, "index.html", locals())
            else :
                #return redirect('/index/')
                return  Server.Transfer("/index#loginModal/")

            

        except:
            errormessage = "error"
        
        return redirect('/index/') #要改  /index#loginModal/沒屁用
    else:
        return render(request, '/index/')

        