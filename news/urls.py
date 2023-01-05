# news/urls.py
from news.views import ArticleViewSet, ReporterViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'articles', ArticleViewSet, basename='article')
router.register(r'reporter', ReporterViewSet, basename='reporter')
urlpatterns = router.urls