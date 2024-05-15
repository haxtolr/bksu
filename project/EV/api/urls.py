from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import AgvViewSet, ArmViewSet, OrderViewSet

router = DefaultRouter()
router.register(r'agv', AgvViewSet, basename='agv')
router.register(r'arms', ArmViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]