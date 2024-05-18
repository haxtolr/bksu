from rest_framework import serializers
from accounts.serializers import UserSerializer
from .models import Agv, Arm, Order, Rack
from products.serializers import ProductSerializer
from django.utils import timezone
from accounts.models import User
from products.models import Product
from .models import Product
import logging

logger = logging.getLogger(__name__)

class AgvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agv
        fields = '__all__'  # 모든 필드를 포함

class ArmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arm
        fields = '__all__'  # 모든 필드를 포함

class RackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rack
        fields = '__all__'  # 모든 필드를 포함

class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.CharField(source='customer.username')  # username 필드만 가져오기
    products = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), many=True)
    agv_id = serializers.SerializerMethodField()
    order_time = serializers.DateTimeField(read_only=True)
    estimated_time = serializers.SerializerMethodField()
    order_number = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['order_number', 'customer', 'products', 'agv_id', 'order_accepted', 'destination', 'order_time', 'estimated_time']

    def get_agv_id(self, obj):
        # 'rd' 상태에 있는 것 중 가장 ID가 낮은 순서에 배당되어 있는 agv_id를 배당
        agv = Agv.objects.filter(status='rd').order_by('id').first()
        return AgvSerializer(agv).data if agv else None

    def get_estimated_time(self, obj):
        # 예상 시간은 order_time에 10분을 더해 저장
        return obj.order_time + timezone.timedelta(minutes=10)

    def get_order_number(self, obj):
        # order_number은 id와 똑같이
        return obj.id
    
    def create(self, validated_data):
        
        customer_data = validated_data.pop('customer')
        products_data = validated_data.pop('products')
        print(validated_data)

        try:
            # User 인스턴스를 찾고
            customer = User.objects.get(username=customer_data['username'])
        except User.DoesNotExist: # 디버깅을 위해 로그생성
            raise serializers.ValidationError("User does not exist")

        # Order 인스턴스를 생성
        order = Order.objects.create(customer=customer, **validated_data)

        # agv_id, estimated_time, order_number 설정
        agv = Agv.objects.filter(status='rd').order_by('id').first()
        order.agv_id = agv if agv else None
        order.estimated_time = order.order_time + timezone.timedelta(minutes=10)
        order.order_number = "#" + str(order.id + 1000)

        # Product 인스턴스를 찾아 Order에 추가.
        for product_data in products_data:
            try:
                product = Product.objects.get(id=product_data.id)
            except Product.DoesNotExist:
                raise serializers.ValidationError("Product does not exist")
            order.products.add(product)

        # 변경 사항 저장
        order.save()
        return order

class OrderSendSerializer(serializers.ModelSerializer):
    customer = serializers.CharField(source='customer.name')
    products = serializers.SerializerMethodField()
    agv_id = serializers.SerializerMethodField()
    order_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M')
    estimated_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M')
    order_number = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['order_number', 'customer', 'products', 'agv_id', 'order_accepted', 'destination', 'order_time', 'estimated_time']

    def get_products(self, obj):
        # 주문에 속한 제품들의 이름만 반환합니다.
        return [product.product_name for product in obj.products.all()]

    def get_agv_id(self, obj):
        # 주문의 AGV ID를 가져옵니다.
        return obj.agv_id.id if obj.agv_id else None

    def get_order_number(self, obj):
        # 주문 번호를 반환합니다.
        return f"#{obj.id + 1000}"  # 예시로 1000을 더해주어 주문 번호 생성
    
