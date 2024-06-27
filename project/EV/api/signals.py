from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .models import Order, Order_Product
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import F
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .models import Order, Order_Product, Agv

@receiver(post_save, sender=Order_Product) 
def order_created(sender, instance, created, **kwargs): 
    if created:
        channel_layer = get_channel_layer()
        order_data = {
            'id': instance.order.id,
            'products': [],
        }
        # Order와 연결된 모든 제품 가져오기
        product_data = {
            'id': instance.product.id,
            'location': instance.product.location_number,
            'quantity': instance.quantity,
        }
        order_data['products'].append(product_data)
        async_to_sync(channel_layer.group_send)(
            'orders',
            {
                'type': 'send_order',
                'order': order_data
            }
        )
        print(f"New order created and sent: {order_data}")

@receiver(post_save, sender=Order)
def post_save_order(sender, instance, **kwargs):
    if instance.order_accepted == 2:
        print(f"Order {instance.id}'s order_accepted changed to 2")
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'orders',
            {
                'type': 'send_message',
                'message': "U"
            }
        )
        print(f"send order_accepted: U")