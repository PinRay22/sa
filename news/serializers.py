from rest_framework import serializers

from myapp.models import order, member
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
import requests




class orderSerializer(serializers.ModelSerializer):
  class Meta:
    model = order
    fields = ['OID', 'Memsanfan', 'Serv', 'SCarbon', 'SPoint', 'OCmp', 'SDATE']
    


  def create(self, validated_data):
    sanfan = validated_data.get('Memsanfan')
    points = validated_data.get('SPoint')
    carbon = validated_data.get('SCarbon')
    user = member.objects.get( Memsanfan = sanfan )
    mpoint = user.MemPoint
    mcarbon = user.MCarbon
    
    member.objects.filter( Memsanfan = sanfan ).update( MemPoint = ( mpoint + points ))
    member.objects.filter( Memsanfan = sanfan ).update( MCarbon = ( mcarbon + carbon ))
    
    return super().create(validated_data)
    
  def back(self):
    return HttpResponseRedirect("https://f120-61-63-97-78.jp.ngrok.io/SA/index.jsp")

#class ReporterSerializer(serializers.ModelSerializer):
#  class Meta:
#    model = Reporter
#    fields = ['name']