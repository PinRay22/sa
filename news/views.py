# news/viewsets.py
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Article, Reporter
from .serializers import ArticleSerializer, ReporterSerializer

class ArticleViewSet(viewsets.ModelViewSet):
  queryset = Article.objects.all()
  serializer_class = ArticleSerializer
  permission_classes = (AllowAny,)

class ReporterViewSet(viewsets.ModelViewSet):
  queryset = Reporter.objects.all()
  serializer_class = ReporterSerializer
  permission_classes = (AllowAny,)