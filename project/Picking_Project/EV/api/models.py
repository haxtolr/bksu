from django.db import models
from accounts.models import User
from products.models import Product
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Agv(models.Model):
    STATUS_CHOICES = [
        ('RD', 'Ready'),
        ('MA', 'Maintenance'), # 유지보수
        ('TG', 'To the destination'), # 도착지로 가는 중
        ('BH', 'Back to home'), # 다시 집으로 오는 중
        ('UL', 'Unloading'), # 물건 하역 중
    ]
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='RD')
    location = models.CharField(max_length=255)
    battery = models.IntegerField()
    order = models.ForeignKey('Order', on_delete=models.SET_NULL, null=True, blank=True)
    last_update = models.DateTimeField(auto_now=True)
    agv_camera = models.CharField(max_length=255, blank=True, null=True)

class Order(models.Model):
    order_number = models.CharField(max_length=255)
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
<<<<<<< HEAD
    products = models.ManyToManyField(Product, through='Order_Product', blank=True)
    agv_id = models.ForeignKey(Agv, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    order_accepted = models.IntegerField(default=0, choices=[(-1, 'Rejected'), (0, 'Pending'), (1, 'Accepted'), (2, 'done'), (3, 'old')])
=======
    products = models.ManyToManyField(Product, blank=True)
    agv_id = models.ForeignKey(Agv, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    order_accepted = models.BooleanField(default=False)
>>>>>>> e5f4478e466ed135085eb68ad645afc355701127
    destination = models.CharField(max_length=255)
    order_time = models.DateTimeField(auto_now=True)
    estimated_time = models.DateTimeField(null=True)

<<<<<<< HEAD
# Order와 Product의 관계를 나타내는 중간 모델
class Order_Product(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

=======
>>>>>>> e5f4478e466ed135085eb68ad645afc355701127
class Arm(models.Model):
    STATUS_CHOICES = [
        ('OP', 'Operating'),  # 작동 중
        ('RD', 'Ready'),  # 대기 중
        ('MA', 'Maintenance'),  # 유지보수 중
    ]
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='ID')
    is_operable = models.BooleanField(default=True)  # 작동 가능 상태
    rack_number = models.IntegerField()  # 부착된 렉 번호
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)  # 작업 중인 주문 번호


class Rack(models.Model):
    STATUS_CHOICES = [
        ('OP', 'Operating'),  # 작동 중
        ('RD', 'Ready'),  # 대기 중
        ('MA', 'Maintenance'),  # 유지보수 중
    ]
    rack_number = models.IntegerField()  # 렉 번호
    products = models.ManyToManyField(Product, blank=True)  # 렉에 있는 상품들
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='RD')  # 렉의 상태
    is_operable = models.BooleanField(default=True)  # 작동 가능 상태
    rack_camera = models.CharField(max_length=255, blank=True, null=True)


class RequestResponse(models.Model):
    REQUEST_TYPE_CHOICES = [
        ('POST', 'POST'),
        ('GET', 'GET'),
    ]
    request_type = models.CharField(max_length=4, choices=REQUEST_TYPE_CHOICES)  # 요청 유형
    target_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    target_object_id = models.PositiveIntegerField()
    target = GenericForeignKey('target_content_type', 'target_object_id')
    request_time = models.DateTimeField(auto_now_add=True)  # 요청 시간
    request_content = models.TextField()  # 요청 내용
    response_content = models.TextField()  # 응답 내용