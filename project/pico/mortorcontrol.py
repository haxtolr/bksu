from machine import Pin, PWM


# PWM 핀 설정
enB = PWM(Pin(20))  # GPIO 15번 핀을 PWM 핀으로 사용
enB.freq(1000)  # PWM 주파수를 1kHz로 설정
in3 = Pin(18, Pin.OUT)  # 방향 제어 핀 1 
in4 = Pin(19, Pin.OUT)  # 방향 제어 핀 2 
speed_HI=65535
speed_Mid=int(65535*0.5)
speed_Low=int(65535*0.2)
set_floor=0


# 엔코더 핀 설정
EV_encorder_pin = Pin(21, Pin.IN, Pin.PULL_DOWN)
GripA_encoder_pin = Pin(13, Pin.IN, Pin.PULL_DOWN)

# 버튼 핀 설정
button_pin_stop = Pin(15, Pin.IN, Pin.PULL_UP)
button_pin_up = Pin(16, Pin.IN, Pin.PULL_UP)
button_pin_down = Pin(17, Pin.IN, Pin.PULL_UP)

def mortor_down(duty_cycle):
    in3.high()
    in4.low()
    enB.duty_u16(duty_cycle)

def mortor_up(duty_cycle):
    in3.low()
    in4.high()
    enB.duty_u16(duty_cycle)

def motor_stop():
    in3.low()
    in4.low()

# 버튼 핀 변경 감지 함수
def stop_button_pressed(button_pin_stop):
    global EV_encoder_value
    global EV_encorder_state
    global set_floor
    EV_encorder_state = True
    EV_encoder_value = 0
    motor_stop()
    print("Button pressed, encoder value reset to 0")
   

def UP_button_pressed(button_pin_up):
    mortor_up(speed_HI)
    print("up")
def DOWN_button_pressed(button_pin_down):
    mortor_down(speed_HI)
    print("down")

#버튼 인터럽트 설정
button_pin_stop.irq(handler=stop_button_pressed, trigger=Pin.IRQ_FALLING)
button_pin_up.irq(handler=UP_button_pressed, trigger=Pin.IRQ_FALLING)
button_pin_down.irq(handler=DOWN_button_pressed, trigger=Pin.IRQ_FALLING)


while True:
    pass