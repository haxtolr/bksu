# views.py
from django.shortcuts import render
from django.http import JsonResponse
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

def send_message_to_clients(message):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'orders',
        {
            'type': 'send_message',
            'message': message,
        }
    )

def index(request):
    return render(request, 'index.html')

def trigger_message(request):
    if request.method == 'POST':
        message = request.POST.get('message', '')
        send_message_to_clients(message)
        return JsonResponse({'status': 'Message sent'})
    else:
        return JsonResponse({'status': 'Invalid request'}, status=400)
