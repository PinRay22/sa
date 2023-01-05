from rest_framework import serializers
from .models import Article, Reporter

class ArticleSerializer(serializers.ModelSerializer):
  class Meta:
    model = Article
    fields = ['id', 'title', 'content', 'created_at', 'updated_at', 'reporter']

class ReporterSerializer(serializers.ModelSerializer):
  class Meta:
    model = Reporter
    fields = ['name']