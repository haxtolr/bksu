from machine import Pin, PWM

GripB_encoder_pin = Pin(10, Pin.IN, Pin.PULL_DOWN)
GripB_encoder_value = 0
GripB_encorder_last_value = 0
GripB_encorder_state = False

def GripB_encoder_changed(GripB_encoder_pin):
    global GripB_encoder_value, GripB_encorder_last_value
    
    if GripB_encorder_state and GripB_encorder_last_value == 1 and GripB_encoder_pin.value() == 0:
        GripB_encoder_value += 1
        print("Encoder value changed:", GripB_encoder_value)
    elif not GripB_encorder_state and GripB_encorder_last_value == 1 and GripB_encoder_pin.value() == 0:
        GripB_encoder_value -= 1
        print("Encoder value changed:", GripB_encoder_value)
        if GripB_encoder_value < 0:
            GripB_encoder_value = 0
            print("NOT INPUT", GripB_encoder_value)
       
    GripB_encorder_last_value = GripB_encoder_pin.value()

GripB_encoder_pin.irq(handler=GripB_encoder_changed, trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING)


while True:
    pass