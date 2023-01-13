"""systemanalyst URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('indexf/', views.start),
    path('acti_p/', views.acti_p),
    path('record_view/', views.record_view),
    path('point_view/', views.point_view),
    path('cmphoto/', views.cmphoto),
    path('vmem_photo/', views.vmem_photo),
    path('pe_view/', views.pe_view),
    path('rede/', views.rede),
    path('index/', views.index),
    path('delete/', views.delete),
    path('exchange/', views.exchange),
    path('alt_view/', views.alt_view),
    path('use_view/', views.use_view),
    path('rank/', views.rank_view),
    path('frank/', views.rank ),
    path('comp_view/', views.comp_view),
    path('insert/', views.insert),
    path('alt_member/', views.alt_member),
    path('vmember/', views.member_view ),
    path('signup_view/', views.signup_view ),
    path('signup/', views.signup ),
    path('logout/', views.logout ),
    path('login_p/', views.login_p ),
    path('login/', views.login_view),
    path('activity/',views.activity_view),
    path('in_progress/', views.in_progress_view),
    path('check/', views.check_mission ),
    path('ck/', views.ck_sighup ),
    path('ck_p/', views.ck_p ),
    path('honor_view/',views.honor_view),
    path('hor_p/',views.honor_p),
    path('lc_view/',views.lc_view),
    path("news/", include("news.urls")),
]
