from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import AgvViewSet, ArmViewSet, OrderViewSet, LatestOrderView
from. views import UserOrdersView, RackViewSet, AllOrdersView
from .views import my_agv

router = DefaultRouter()
router.register(r'agv', AgvViewSet, basename='agv')
router.register(r'arms', ArmViewSet)
router.register(r'racks', RackViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('latest_order/<str:username>/', LatestOrderView.as_view()),  # 새로운 경로 추가
    path('user_orders/<str:username>/', UserOrdersView.as_view(), name='user_orders'),
    path('allorders/', AllOrdersView.as_view(), name='all_orders'),
    path('send_agv/', my_agv),
      # 완료 명령을 받는 경로 추가
]
