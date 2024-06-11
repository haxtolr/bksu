from rest_framework import serializers
from .models import Agv, Arm, Order, Rack, Order_Product
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

class OrderProductSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(source='product.id')
    quantity = serializers.IntegerField()

    class Meta:
        model = Order_Product
        fields = ['product_id', 'quantity']

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

        try:
            # User 인스턴스를 찾고
            customer = User.objects.get(username=customer_data['username'])
        except User.DoesNotExist: # 디버깅을 위해 로그생성
            raise serializers.ValidationError("User does not exist")

        # Order 인스턴스를 생성
        order = Order.objects.create(customer=customer, **validated_data)

        # agv_id, estimated_time, order_number 설정
        agv = Agv.objects.filter(status='rd').order_by('id').first()
        if agv:
        # agv의 order_id 필드를 업데이트
            agv.order_id = order.id
            agv.save()
        else:
            logger.info("No available AGV")
            raise serializers.ValidationError("No available AGV")
        order.agv_id = agv if agv else None
        order.estimated_time = order.order_time + timezone.timedelta(minutes=10)
        order.order_number = "#" + str(order.id + 1000)
        if not order.order_number:
                raise serializers.ValidationError("Order number is not set")
        # Product 인스턴스를 찾아 Order에 추가.
        product_ids = [product_data.id for product_data in products_data]  # Product 객체의 id만을 담은 리스트 생성
        unique_product_ids = set(product_ids)  # 중복을 제거한 Product id 리스트 생성

        for unique_id in unique_product_ids:
            try:
                product = Product.objects.get(id=unique_id)
            except Product.DoesNotExist:
                raise serializers.ValidationError("Product does not exist")

            product_count = product_ids.count(unique_id)  # 특정 Product 객체가 몇 번 등장하는지 세기
            Order_Product.objects.create(order=order, product=product, quantity=product_count)  # OrderProduct 인스턴스 생성 및 저장
            product.quantity -= product_count
            if product.quantity < 0:
                raise serializers.ValidationError("Not enough product in stock")
            product.save()
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
    agv = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['order_number', 'customer', 'products', 'agv_id', 'agv','order_accepted', 'destination', 'order_time', 'estimated_time']

    def get_products(self, obj):
        # 주문에 속한 제품들의 이름만 반환합니다.
        order_products = Order_Product.objects.filter(order=obj)  # 해당 주문에 대한 OrderProduct 객체들을 가져옵니다.
        return [{"name": order_product.product.product_name, "quantity": order_product.quantity} for order_product in order_products]
    
    def get_agv_id(self, obj):
        # 주문의 AGV ID를 가져옵니다.
        return obj.agv_id.id if obj.agv_id else None
    
    def get_agv(self, obj):
        if obj.agv_id:
            return AgvSerializer(obj.agv_id).data
        return None
    
    def get_order_number(self, obj):
        # 주문 번호를 반환합니다.
        return f"#{obj.id + 1000}"  # 예시로 1000을 더해주어 주문 번호 생성
    

class OrderListSerializer(serializers.ModelSerializer):
    customer = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    products = serializers.SerializerMethodField()  # SerializerMethodField로 변경
    agv_id = serializers.PrimaryKeyRelatedField(queryset=Agv.objects.all())
    
    class Meta:
        model = Order
        fields = ['id', 'customer', 'products', 'agv_id', 'order_accepted', 'destination', 'order_time', 'estimated_time', 'order_number']

    def get_products(self, obj):
        # 주문에 속한 제품들의 이름과 수량을 반환
        order_products = Order_Product.objects.filter(order=obj)  # 해당 주문에 대한 OrderProduct 객체
        return [{"name": order_product.product.product_name, "quantity": order_product.quantity} for order_product in order_products]

from collections import defaultdict

class OrderProductCountSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(source='product.id')
    quantity = serializers.IntegerField()

    class Meta:
        model = Order_Product
        fields = ['product_id', 'quantity']

    def get_order_counts(self):
        # 모든 Order_Product 인스턴스를 가져옵니다.
        order_products = Order_Product.objects.all()

        # 각 상품이 주문된 총 수량을 계산합니다.
        product_counts = defaultdict(int)
        for order_product in order_products:
            product_counts[order_product.product.id] += order_product.quantity

        # 상품 ID와 해당 상품이 주문된 총 수량을 쌍으로 하는 딕셔너리를 반환합니다.
        return dict(product_counts)
