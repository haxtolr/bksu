from rest_framework import viewsets, status
from .serializers import AgvSerializer, ArmSerializer, OrderSerializer
from .serializers import OrderProductCountSerializer, OrderSendSerializer, RackSerializer, OrderListSerializer
from .models import Agv, Arm, Order, Rack, Order_Product
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse

class AgvViewSet(viewsets.ModelViewSet):
    queryset = Agv.objects.all()
    serializer_class = AgvSerializer

class ArmViewSet(viewsets.ModelViewSet):
    queryset = Arm.objects.all()
    serializer_class = ArmSerializer

class RackViewSet(viewsets.ModelViewSet):
    queryset = Rack.objects.all()
    serializer_class = RackSerializer
    
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

class LatestOrderView(APIView):
    def get(self, request, username, format=None):
        # 사용자의 모든 주문을 가져옴
        orders = Order.objects.filter(customer__username=username).order_by('-order_time')
        if orders.exists():
            # 가장 최근의 주문을 선택합니다.
            latest_order = orders.first()
            # 선택한 주문을 직렬화합니다.
            serializer = OrderSendSerializer(latest_order)
            return Response(serializer.data)
        else:
            return Response({"message": "No orders found for this user."})
    
    def patch(self, request, username, format=None):
        # 사용자의 모든 주문을 가져옴
        orders = Order.objects.filter(customer__username=username).order_by('-order_time')
        if orders.exists():
            # 가장 최근의 주문을 선택합니다.
            latest_order = orders.first()
            latest_order.order_accepted = request.data.get('order_accepted', latest_order.order_accepted)
            latest_order.save()
            return(Response({"message": "Order updated."}))
        return Response({"message": "No orders found for this user."})

class UserOrdersView(APIView):
    def get(self, request, username, format=None):
        # 사용자의 최근 순서로 모든 주문을 가져옵니다.
        orders = Order.objects.filter(customer__username=username).order_by('-order_time')
        if orders.exists():
            # 모든 주문을 직렬화합니다.
            serializer = OrderSendSerializer(orders, many=True)
            return Response(serializer.data)
        else:
            return Response({"message": "No orders found for this user."}, status=status.HTTP_404_NOT_FOUND)

class AllOrdersView(APIView):
    def get(self, request, format=None):
        # 모든 주문을 가져옵니다.
        orders = Order.objects.all()
        # 주문을 직렬화합니다.
        serializer = OrderListSerializer(orders, many=True)
        return Response(serializer.data)

class ProductCountView(APIView): ### 그래프 고민해야댐
    def get(self, request, format=None):
        ProductCount = OrderProductCountSerializer(Order_Product.objects.all(), many=True)
        return Response(ProductCount.data)


def my_agv(request):
    # agv_id가 1인 주문 중 id 값이 가장 낮은 주문을 가져옵니다.
    order = Order.objects.filter(agv_id=1).order_by('id').first()

    if order is not None:
        # 주문을 직렬화합니다.
        serializer = OrderSerializer(order)
        my_data = {'order': serializer.data}
    else:
        my_data = {'message': 'No order found'}

    return JsonResponse(my_data)
