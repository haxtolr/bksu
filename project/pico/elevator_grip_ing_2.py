from machine import Pin, PWM
import utime
import time
import sys


#층수 타켓 설정
floor_target_1=16
floor_target_2=87
floor_target_3= 167

# PWM 핀 설정
enB = PWM(Pin(20))  # GPIO 15번 핀을 PWM 핀으로 사용
enB.freq(1000)  # PWM 주파수를 1kHz로 설정
in3 = Pin(18, Pin.OUT)  # 방향 제어 핀 1 
in4 = Pin(19, Pin.OUT)  # 방향 제어 핀 2 
speed_HI=65535
speed_Mid=int(65535*0.5)
speed_Low=int(65535*0.2)
set_floor=0
start_time = utime.ticks_ms()

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


# 엔코더 핀 설정
EV_encorder_pin = Pin(21, Pin.IN, Pin.PULL_DOWN)
GripA_encoder_pin = Pin(13, Pin.IN, Pin.PULL_DOWN)

# # 버튼 핀 설정
# button_pin_stop = Pin(15, Pin.IN, Pin.PULL_UP)
# button_pin_up = Pin(16, Pin.IN, Pin.PULL_UP)
# button_pin_down = Pin(17, Pin.IN, Pin.PULL_UP)


# 전역 변수 선언
load_state=False

EV_encoder_value = 0
EV_encorder_last_value = 0
EV_encorder_state = False

GripA_encoder_value = 0
GripA_encorder_last_value = 0
GripA_encoder_state = False #true-> 증가방향 false-> 감소방향

GripB_encoder_value = 0
GripB_encorder_last_value = 0
GripB_encorder_state = False

STEP_state=0
arm_done = False

# 엔코더 핀 변경 감지 함수
def EV_encoder_changed(EV_encorder_pin):
    global EV_encoder_value, EV_encorder_last_value
    
    if EV_encorder_state and EV_encorder_last_value == 1 and EV_encorder_pin.value() == 0:
        EV_encoder_value += 1
        print("Encoder value changed:", EV_encoder_value)
    elif not EV_encorder_state and EV_encorder_last_value == 1 and EV_encorder_pin.value() == 0:
        EV_encoder_value -= 1
        print("Encoder value changed:", EV_encoder_value)
        if EV_encoder_value < -20:
            EV_encoder_value = -21
            motor_stop()
            print("NOT INPUT", EV_encoder_value)
       
    EV_encorder_last_value = EV_encorder_pin.value()

#그립A
def GripA_encoder_changed(GripA_encoder_pin):
    global GripA_encoder_value, GripA_encorder_last_value,load_state
    
    if GripA_encoder_state and GripA_encorder_last_value == 1 and GripA_encoder_pin.value() == 0:
        GripA_encoder_value += 1
        print("GripA_Encoder value changed:", GripA_encoder_value)
    elif not GripA_encoder_state and GripA_encorder_last_value == 1 and GripA_encoder_pin.value() == 0:
        GripA_encoder_value -= 1
        print("GripA_Encoder value changed:", GripA_encoder_value)
        if GripA_encoder_value < 0:
            GripA_encoder_value = -1
            print("GripA_NOT INPUT", GripA_encoder_value)
       
    GripA_encorder_last_value = GripA_encoder_pin.value()


# # 버튼 핀 변경 감지 함수
# def stop_button_pressed(button_pin_stop):
#     global EV_encoder_value
#     global EV_encorder_state
#     global set_floor
#     EV_encorder_state = True
#     EV_encoder_value = 0
#     motor_stop()
#     print("Button pressed, encoder value reset to 0")
#     set_floor = int(input("Set the floor: "))

# def UP_button_pressed(button_pin_up):
#     mortor_up(speed_HI)
#     print("up")
# def DOWN_button_pressed(button_pin_down):
#     mortor_down(speed_HI)
#     print("down")
   
    
def floor_set():
    
    global set_floor,EV_encorder_state,EV_encoder_value,load_state,STEP_state

    motor_stop()
    print(f"{set_floor}: floor")
    load_state=True

    # while True:

    #     if GripA_encoder_value == 10:
    #         load_state=False 
    #         break
    print("wait 3 seconds")  
    time.sleep(3) # 작업 
    print("LOAD_complete")

    EV_encorder_state = False
    mortor_down(speed_HI)

    while True:
        if EV_encoder_value <=-20:
            motor_stop()
            break
    
    set_floor = 0
    STEP_state =1
    
     


# 엔코더 인터럽트 설정
EV_encorder_pin.irq(handler=EV_encoder_changed, trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING)
GripA_encoder_pin.irq(handler=GripA_encoder_changed, trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING)

# #버튼 인터럽트 설정
# button_pin_stop.irq(handler=stop_button_pressed, trigger=Pin.IRQ_FALLING)
# button_pin_up.irq(handler=UP_button_pressed, trigger=Pin.IRQ_FALLING)
# button_pin_down.irq(handler=DOWN_button_pressed, trigger=Pin.IRQ_FALLING)

#초기값 설정
motor_stop()

# 메인 루프
while True:
   
   #1초마다 엘레베이터 엔코더 벨류 프린트    
    current_time = utime.ticks_ms()
    if utime.ticks_diff(current_time, start_time) >= 1000:
        print("Encoder value:", EV_encoder_value)
        start_time = current_time
    #층수 입력
    if STEP_state== 0: 
        if set_floor == 0 :
            motor_stop()
            while True:
                set_floor = int(input("Set the floor: "))
                if set_floor >3:
                    print("not vaild")
                else: 
                    EV_encorder_state = True
                    break
    
    #층수값받으면 시작
        mortor_up(speed_HI)
        if set_floor == 1:    
            if EV_encoder_value >= floor_target_1 and EV_encoder_value < floor_target_1+5:
                    floor_set()
                
        elif set_floor == 2:
            if EV_encoder_value >= floor_target_2 and EV_encoder_value < floor_target_2+5:
                    floor_set()
        elif set_floor == 3:
            if EV_encoder_value >= floor_target_3 and EV_encoder_value < floor_target_3+5:
                    floor_set()


    if STEP_state == 1:
        
        EV_encorder_state = True
        while True and not arm_done:
            utime.sleep(5)
            arm_done = True
            break
            

        mortor_up(speed_HI)
        if EV_encoder_value >=2:
            EV_encoder_value=0
            motor_stop()
            STEP_state=0
            

    if STEP_state==2:
        print("done")
        utime.sleep(1)
        
        