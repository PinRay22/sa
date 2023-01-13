# news/viewsets.py
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .serializers import orderSerializer
from myapp.models import order
from django.http import HttpResponse, HttpResponseRedirect, Http404

def back(self):
    return HttpResponseRedirect("https://f120-61-63-97-78.jp.ngrok.io/SA/index.jsp")

class orderViewSet(viewsets.ModelViewSet):
  queryset = order.objects.all()
  serializer_class = orderSerializer
  permission_classes = (AllowAny,)

  def back(self):
    return HttpResponseRedirect("https://f120-61-63-97-78.jp.ngrok.io/SA/index.jsp")


class testViewSet(viewsets.ModelViewSet):
  queryset = order.objects.all()
  serializer_class = orderSerializer
  permission_classes = (AllowAny,)

