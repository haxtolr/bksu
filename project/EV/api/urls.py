from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import AgvViewSet, ArmViewSet, OrderViewSet, LatestOrderView, UserOrdersView, RackViewSet

router = DefaultRouter()
router.register(r'agv', AgvViewSet, basename='agv')
router.register(r'arms', ArmViewSet)
router.register(r'racks', RackViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('latest_order/<str:username>/', LatestOrderView.as_view()),  # 새로운 경로 추가
    path('user_orders/<str:username>/', UserOrdersView.as_view(), name='user_orders'),
]