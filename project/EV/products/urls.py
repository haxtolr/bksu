from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('upload/', views.upload_image, name='upload_image'),
    path('getpro/', views.ProductViewSet.as_view({'get': 'list'}), name='products')
    # 다른 URL 패턴들...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)