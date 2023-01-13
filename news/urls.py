# news/urls.py
from news.views import orderViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'order', orderViewSet, basename='order')
urlpatterns = router.urls