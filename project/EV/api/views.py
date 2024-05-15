from rest_framework import viewsets, status
from .serializers import AgvSerializer, ArmSerializer, OrderSerializer
from .models import Agv, Arm, Order
from rest_framework.response import Response
from django.utils import timezone
from rest_framework.permissions import IsAuthenticated



class AgvViewSet(viewsets.ModelViewSet):
    queryset = Agv.objects.all()
    serializer_class = AgvSerializer

class ArmViewSet(viewsets.ModelViewSet):
    queryset = Arm.objects.all()
    serializer_class = ArmSerializer

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