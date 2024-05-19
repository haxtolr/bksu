from rest_framework import viewsets, status
from .serializers import AgvSerializer, ArmSerializer, OrderSerializer, OrderSendSerializer, RackSerializer
from .models import Agv, Arm, Order, Rack
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

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
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            print("serializer.errors: ", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # 유효성 검사를 통과한 경우에만 새로운 주문을 생성합니다.
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    

class LatestOrderView(APIView):
    def get(self, request, username, format=None):
        # 사용자의 모든 주문을 가져옵니다.
        orders = Order.objects.filter(customer__username=username).order_by('-order_time')
        if orders.exists():
            # 가장 최근의 주문을 선택합니다.
            latest_order = orders.first()
            # 선택한 주문을 직렬화합니다.
            serializer = OrderSendSerializer(latest_order)
            return Response(serializer.data)
        else:
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

