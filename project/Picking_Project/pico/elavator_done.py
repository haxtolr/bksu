from machine import Pin, PWM
import utime
import time
import sys

# PWM 핀 설정
enB = PWM(Pin(20))  # GPIO 15번 핀을 PWM 핀으로 사용
enB.freq(1000)  # PWM 주파수를 1kHz로 설정
in3 = Pin(18, Pin.OUT)  # 방향 제어 핀 1 
in4 = Pin(19, Pin.OUT)  # 방향 제어 핀 2 
speed_HI=65535
speed_Mid=65535*0.5
speed_Low=65535*0.2
set_floor=0

def motor_forward(duty_cycle):
    in3.high()
    in4.low()
    enB.duty_u16(duty_cycle)

def motor_backward(duty_cycle):
    in3.low()
    in4.high()
    enB.duty_u16(duty_cycle)

def motor_stop():
    in3.low()
    in4.low()


# 엔코더 핀 설정
encoder_pin = Pin(21, Pin.IN, Pin.PULL_DOWN)

# 버튼 핀 설정
button_pin = Pin(15, Pin.IN, Pin.PULL_UP)

# 전역 변수 선언
EV_encoder_value = 0
EV_encorder_last_value = 0
encoder_state = False

GripA_encoder_value = 0
GripA_encorder_last_value = 0
GripB_encoder_value = 0
GripB_encorder_last_value = 0


# 엔코더 핀 변경 감지 함수
def encoder_changed(encoder_pin):
    global EV_encoder_value, EV_encorder_last_value
    
    if encoder_state and EV_encorder_last_value == 1 and encoder_pin.value() == 0:
        EV_encoder_value += 1
        print("Encoder value changed:", EV_encoder_value)
    elif not encoder_state and EV_encorder_last_value == 1 and encoder_pin.value() == 0:
        EV_encoder_value -= 1
        print("Encoder value changed:", EV_encoder_value)
        if EV_encoder_value < 0:
            EV_encoder_value = 0
            print("NOT INPUT", EV_encoder_value)
       
    EV_encorder_last_value = encoder_pin.value()

# 버튼 핀 변경 감지 함수
def button_pressed(button_pin):
    global EV_encoder_value
    global encoder_state
    global set_floor
    encoder_state = True
    EV_encoder_value = 0
    motor_stop()
    print("Button pressed, encoder value reset to 0")
    set_floor = int(input("Set the floor: "))
    
def floor_set():

   
    global set_floor
    global encoder_state
    global EV_encoder_value

    motor_stop()
    print(f"{set_floor}: floor")
    time.sleep(3)  # 작업 
    print("work_done")
    encoder_state = False
    motor_backward(speed_HI)

    while True:
        if EV_encoder_value == 0:
            motor_stop()
            break
    
    set_floor = 0
    floor_set_DONE =True
    
    return floor_set_DONE 


# 엔코더 인터럽트 설정
encoder_pin.irq(handler=encoder_changed, trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING)

# 버튼 인터럽트 설정
button_pin.irq(handler=button_pressed, trigger=Pin.IRQ_FALLING)


# 메인 루프
while True:
    
    if set_floor == 0 :
        motor_stop()
        set_floor = int(input("Set the floor: "))
        encoder_state = True
    utime.sleep(1)  # 1초마다 출력 확인
    print("Encoder value:", EV_encoder_value)
    motor_forward(speed_HI)
    if set_floor == 1:    
          if EV_encoder_value >= 10 and EV_encoder_value < 15:
                floor_set()
    elif set_floor == 2:
          if EV_encoder_value >= 20 and EV_encoder_value < 25:
                floor_set()
    elif set_floor == 3:
         if EV_encoder_value >= 30 and EV_encoder_value < 35:
                floor_set()