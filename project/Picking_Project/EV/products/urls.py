<<<<<<< HEAD
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('products', views.ProductViewSet, basename='product')

urlpatterns = [
    path('upload/', views.upload_image, name='upload_image'),
    path('getpro/', views.ProductViewSet.as_view({'get': 'list'}), name='getpro'),
    path('', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('upload/', views.upload_image, name='upload_image'),
    path('getpro/', views.ProductViewSet.as_view({'get': 'list'}), name='products')
    # 다른 URL 패턴들...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> e5f4478e466ed135085eb68ad645afc355701127
