from rest_framework import viewsets, status
from .serializers import AgvSerializer, ArmSerializer, OrderSerializer, OrderSendSerializer, RackSerializer, OrderListSerializer
from .models import Agv, Arm, Order, Rack, Order_Product
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.shortcuts import render
import socket
from collections import Counter
import logging

logger = logging.getLogger(__name__)

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
            print("serializer.errors: ", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # 유효성 검사를 통과한 경우에만 새로운 주문을 생성
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
class LatestOrderView(APIView):
    def get(self, request, username, format=None):
        # 사용자의 모든 주문을 가져옴
        orders = Order.objects.filter(customer__username=username).order_by('-order_time')
        if orders.exists():
            # 가장 최근의 주문을 선택합니다.
            latest_order = orders.first()
            # 선택한 주문을 직렬화합니다.
            serializer = OrderSendSerializer(latest_order)
            print(serializer.data)
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

class AllOrdersView(APIView):
    def get(self, request, format=None):
        # 모든 주문을 가져옵니다.
        orders = Order.objects.all()
        # 주문을 직렬화합니다.
        serializer = OrderListSerializer(orders, many=True)
        return Response(serializer.data)


def pico_control(request):
    if request.method == 'POST':
        value = request.POST.get('value')  # 클라이언트에서 전달된 값

        try:
            # 피코 서버와 소켓 연결
            pico_host = '172.30.1.63'  # 피코 서버의 IP 주소로 변경하세요
            pico_port = 5000
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((pico_host, pico_port))

            # 피코 서버로 값 전송
            client_socket.send(value.encode())

            # 피코 서버로부터 응답 받기
            response = client_socket.recv(1024).decode()
            client_socket.close()

            return render(request, 'control.html', {'message': response})
        except socket.error as e:
            return render(request, 'control.html', {'error_message': '피코 서버와의 연결에 문제가 발생했습니다.'})
    else:
        return render(request, 'control.html')