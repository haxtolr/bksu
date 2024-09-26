from machine import Pin, PWM

GripA_encoder_pin = Pin(6, Pin.IN, Pin.PULL_DOWN)
GripA_encoder_value = 0
GripA_encorder_last_value = 0
GripA_encoder_state = True

def EV_encoder_changed(GripA_encoder_pin):
    global GripA_encoder_value, GripA_encorder_last_value
    
    if GripA_encoder_state and GripA_encorder_last_value == 1 and GripA_encoder_pin.value() == 0:
        GripA_encoder_value += 1
        print("Encoder value changed:", GripA_encoder_value)
    elif not GripA_encoder_state and GripA_encorder_last_value == 1 and GripA_encoder_pin.value() == 0:
        GripA_encoder_value -= 1
        print("Encoder value changed:", GripA_encoder_value)
        if GripA_encoder_value < 0:
            GripA_encoder_value = 0
            print("NOT INPUT", GripA_encoder_value)
       
    GripA_encorder_last_value = GripA_encoder_pin.value()

GripA_encoder_pin.irq(handler=EV_encoder_changed, trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING)


while True:
    pass