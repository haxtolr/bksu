import paho.mqtt.client as mqtt

mqtt = mqtt.Client("python_pub")  # callback_api_version 추가
mqtt.connect("172.30.1.20", 1883)

mqtt.publish("/Robot/123/speed", "2조")

mqtt.loop(2)