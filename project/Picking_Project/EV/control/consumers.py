from channels.generic.websocket import WebsocketConsumer
from channels.layers import get_channel_layer
import json
from asgiref.sync import async_to_sync
from api.models import Order, Agv


agv_step = 0

class controlConsumer(WebsocketConsumer):
    class_agv_order_id = None
    class_agv_id = None
    def connect(self):
        self.group_name = 'orders'
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )
        self.accept()
        print(f"Connected to WebSocket with channel name: {self.channel_name}")

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
        )
        print(f"Disconnected from WebSocket with channel name: {self.channel_name}")

    def receive(self, text_data):
        global agv_step

        print(f"Received text data: {text_data}")
        data = json.loads(text_data)
        print(data)
        message = data.get('message', '')
        if 'agv' in message:
            aid, _ = message.split('agv')
            id = aid.strip('_')
            print(id)
            order = Order.objects.get(id=id)
            controlConsumer.class_agv_order_id = id
            agv = Agv.objects.get(id=order.agv_id.id)
            controlConsumer.class_agv_id = agv.id
            print(f"recv : agv message")
            if 'agv_go' in message:
                agv.status = 'TG'
                destination = order.destination
                agv.location = "40%"
                agv.save()
                id_destination = "{}_{}".format(id, destination)
                channel_layer = get_channel_layer()
                async_to_sync(channel_layer.group_send)(
                    'orders',
                    {
                        'type': 'send_message',
                        'message': id_destination,
                    }
                )
            elif 'agv_arrived' in message:
                print(f"agv_arrived")
                print(f"agv_id : {agv.id}")
                agv_step = 0
                order.order_accepted = 1
                order.save()
                agv.status = 'UL'
                agv.location = "100%"
                agv.save()
                
            elif 'agv_return' in message:
                agv.status = 'BH'
                agv.save()
                
            elif 'agv_home' in message:
                agv.status = 'RD'
                agv.location = "0%"
                agv.battery = 83
                agv.save()
                
            elif 'agv_step_' in message:
                if agv_step == 0:
                    agv.location = "60%"
                elif agv_step == 1:
                    agv.location = "80%"
                agv_step += 1
                agv.save()
                

    def send_order(self, event):
        order = event['order']
        self.send(text_data=json.dumps({
            'order': order
        }))
        print(f"Sent order to WebSocket: {order}")

    def send_message(self, message):
        self.send(text_data=json.dumps({
            'message': message
        }))
        print(f"Sent message to WebSocket: {message}")