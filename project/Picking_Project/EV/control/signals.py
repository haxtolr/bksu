from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from api.models import Order

@receiver(post_save, sender=Order)
def order_created(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        order_data = {
            'id': instance.id,
            'product': instance.product.name,
            'quantity': instance.quantity
        }
        async_to_sync(channel_layer.group_send)(
            'orders',
            {
                'type': 'send_order',
                'order': order_data
            }
        )
        print(f"New order created and sent: {order_data}")
