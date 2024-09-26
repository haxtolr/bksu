from machine import Pin, PWM
import utime
import time
import sys

#층수 타켓 설정
floor_target_1=17
floor_target_2=87
floor_target_3= 164

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
GripB_encoder_pin = Pin(6, Pin.IN, Pin.PULL_DOWN)

# 전역 변수 선언
load_state=False

EV_encoder_value = 0
EV_encorder_last_value = 0
EV_encorder_state = False

GripA_encoder_pin = Pin(10, Pin.IN, Pin.PULL_DOWN)
GripA_encoder_value = 0
GripA_encorder_last_value = 0
GripA_encoder_state = False #true-> 증가방향 false-> 감소방향

GripB_encoder_pin = Pin(6, Pin.IN, Pin.PULL_DOWN)
GripB_encoder_value = 0
GripB_encorder_last_value = 0
GripB_encoder_state = False

STEP_state=0

# 서보 모터의 주기 설정 (주파수: 50Hz, 주기: 20ms)
servo_freq=50
# 서보 모터 핀 설정
A_servo_front=PWM(Pin(12))
B_servo_front=PWM(Pin(8))
# 각 서보 모터의 주파수 설정
A_servo_front.freq(servo_freq)
B_servo_front.freq(servo_freq)

# 서보 모터의 주기 설정 (주파수: 50Hz, 주기: 20ms)
servo_freq=50
# 서보 모터 핀 설정
A_servo=PWM(Pin(11))
B_servo=PWM(Pin(7))
# 각 서보 모터의 주파수 설정
A_servo.freq(servo_freq)
B_servo.freq(servo_freq)

# 앞 서보모터
A_servo_front=PWM(Pin(12))
B_servo_front=PWM(Pin(8))
# 각 서보 모터의 주파수 설정
A_servo_front.freq(servo_freq)
B_servo_front.freq(servo_freq)

def set_servo_angle(servo_pin, angle):
    # 0도: 0.5ms (65535 * 0.5ms / 20ms = 1638)
    # 180도: 2.5ms (65535 * 2.5ms / 20ms = 8191)
    MIN_DUTY = 1638
    MAX_DUTY = 8191
    # 각도를 PWM 신호로 변환하여 서보 모터 각도 설정
    duty = int(MIN_DUTY + (MAX_DUTY - MIN_DUTY) * (angle / 180))
    servo_pin.duty_u16(duty)

def set_servo_speed(servo_pin, speed):
    # 0도: 0.5ms (65535 * 0.5ms / 20ms = 1638)
    # 180도: 2.5ms (65535 * 2.5ms / 20ms = 8191)
 
    stop_duty = 4915
    min_duty = 1638
    max_duty = 8191 

    duty = int(stop_duty + (max_duty - stop_duty) * (speed / 100))
    servo_pin.duty_u16(duty)

# 엔코더 핀 변경 감지 함수
def EV_encoder_changed(EV_encorder_pin):
    global EV_encoder_value, EV_encorder_last_value
    
    if EV_encorder_state and EV_encorder_last_value == 1 and EV_encorder_pin.value() == 0:
        EV_encoder_value += 1
        #print("Encoder value changed:", EV_encoder_value)
    elif not EV_encorder_state and EV_encorder_last_value == 1 and EV_encorder_pin.value() == 0:
        EV_encoder_value -= 1
        #print("Encoder value changed:", EV_encoder_value)
        if EV_encoder_value < -20:
            EV_encoder_value = -21
            motor_stop()
            print("NOT INPUT", EV_encoder_value)
       
    EV_encorder_last_value = EV_encorder_pin.value()

#그립A
def GripA_encoder_changed(GripA_encoder_pin):
    global GripA_encoder_value, GripA_encorder_last_value,load_state
    
    if load_state: 
        if  GripA_encoder_state and GripA_encorder_last_value == 1 and GripA_encoder_pin.value() == 0:
            GripA_encoder_value += 1
            #print("a_Encoder value changed:", GripA_encoder_value)
        elif not GripA_encoder_state and GripA_encorder_last_value == 1 and GripA_encoder_pin.value() == 0:
            GripA_encoder_value -= 1
            #print("a_Encoder value changed:", GripA_encoder_value)
            if GripA_encoder_value < 0:
                GripA_encoder_value = 0
                print("a_NOT INPUT", GripA_encoder_value)
       
    GripA_encorder_last_value = GripA_encoder_pin.value()

#그립B
def GripB_encoder_changed(GripB_encoder_pin):
    global GripB_encoder_value, GripB_encorder_last_value,load_state
    if load_state:
        if GripB_encoder_state and GripB_encorder_last_value == 1 and GripB_encoder_pin.value() == 0:
            GripB_encoder_value += 1
            #print("B_Encoder value changed:", GripB_encoder_value)
        elif not GripB_encoder_state and GripB_encorder_last_value == 1 and GripB_encoder_pin.value() == 0:
            GripB_encoder_value -= 1
            #print("B_Encoder value changed:", GripB_encoder_value)
            if GripB_encoder_value < 0:
                GripB_encoder_value = 0
                print("B_NOT INPUT", GripB_encoder_value)

    GripB_encorder_last_value = GripB_encoder_pin.value()
    
def floor_set():
    
    global set_floor,EV_encorder_state,EV_encoder_value,load_state,STEP_state
    global GripA_encoder_state,GripB_encoder_state
    global GripA_encoder_value,GripB_encoder_value

    motor_stop()
    print(f"{set_floor}: floor")
    load_state=True

    print("wait 3 seconds")  
    time.sleep(3) # 해당 층에 작업 대기
    while True:
        target1=81
        target2=1
        GripA_encoder_state = True
        GripB_encoder_state = True

        set_servo_speed(A_servo,-100)   #a기준: -100 앞으로
        set_servo_speed(B_servo,100)  #b기준: 100 앞으로
        print("girp _forward")
        a_set = True 
        b_set = True
        #그리퍼 앞으로가서 멈추는 함수
        while True: 
            while True:
                if  GripA_encoder_value>=target1:
                    set_servo_speed(A_servo,0)
                    print(f"A1 : {GripA_encoder_value}")
                    a_set = False
                if  GripB_encoder_value>=target1:
                    set_servo_speed(B_servo,0)
                    print(f"B1 : {GripB_encoder_value}")
                    b_set = False
                if a_set == False and b_set == False:
                    break

            if GripA_encoder_value >=target1+1 and GripB_encoder_value>= target1+1:
                set_servo_speed(A_servo,0)
                set_servo_speed(B_servo,0)
                print(f"A : {GripA_encoder_value}")
                print(f"B : {GripB_encoder_value}")
                break
        print("grip stop") # 앞에서 스탑
        utime.sleep(2)
    
        #서보들을 0도로 회전
        set_servo_angle(A_servo_front, 90)
        set_servo_angle(B_servo_front, 0)
        print("girp on")
        utime.sleep(2)  # 2초 대기
        #그리퍼 당기기 상태
        GripA_encoder_state = False
        GripB_encoder_state = False

        set_servo_speed(A_servo,100)    #a기준: 100 뒤로
        set_servo_speed(B_servo,-100)   #b기준: -100 뒤로
        a_set = True 
        b_set = True
        # 그리퍼 당기기
        while True:
            while True:
                if  GripA_encoder_value == target2:
                    set_servo_speed(A_servo,0)
                    print(f"A2 : {GripA_encoder_value}")
                    a_set = False
                if  GripB_encoder_value == target2:
                    set_servo_speed(B_servo,0)
                    print(f"B2 : {GripB_encoder_value}")
                    b_set = False
                if a_set == False and b_set == False :
                    break
            if GripA_encoder_value <=target2 and GripB_encoder_value<= target2:
                set_servo_speed(A_servo,0)
                set_servo_speed(B_servo,0)
                print(f"A : {GripA_encoder_value}")
                print(f"B : {GripB_encoder_value}")
                break
        GripA_encoder_state = True
        GripB_encoder_state = True        
        break

    utime.sleep(3)
    load_state=False
    print("LOAD_complete") # 엘레베이터에 적재 완료

    EV_encorder_state = False
    mortor_down(speed_HI)

    # 0층으로 도착후 정지
    while True:
        if EV_encoder_value <=-20:
            motor_stop()
            break
    
    ### 암 통신 을
    STEP_state = 1

    if STEP_state == 1:
        # 암동작후
        EV_encorder_state = True
        test_arm = input("arm ok? : ")
        if test_arm == "ok":
            utime.sleep(2)
    ######
        mortor_up(speed_HI) # 가져다 놓기
        # 해당층에 멈춤
        while True:
            if set_floor == 1:    
                if EV_encoder_value >= floor_target_1+4 and EV_encoder_value < floor_target_1+6:
                    motor_stop()
                    break                
            elif set_floor == 2:
                if EV_encoder_value >= floor_target_2+4 and EV_encoder_value < floor_target_2+6:
                    motor_stop()
                    break
            elif set_floor == 3:
                if EV_encoder_value >= floor_target_3+4 and EV_encoder_value < floor_target_3+6:
                    motor_stop()
                    break
        
        print(f"{set_floor}: floor") # 해당층 도착
        load_state=True # 다시 넣겠다.

        print("wait 3 seconds")  
        time.sleep(3) # 넣는 작업 
        while True:
            target1=81
            target2=1
            GripA_encoder_state = True
            GripB_encoder_state = True

            set_servo_speed(A_servo,-100)   #a기준: -100 앞으로
            set_servo_speed(B_servo,100)  #b기준: 100 앞으로
            print("girp _forward")
            a_set = True
            b_set = True
            # 그리퍼 앞으로 전진
            while True:
                while True:
                    if  GripA_encoder_value==target1:
                        set_servo_speed(A_servo,0)
                        print(f"A3 : {GripA_encoder_value}")
                        a_set = False
                    if  GripB_encoder_value==target1:
                        set_servo_speed(B_servo,0)
                        print(f"B3 : {GripB_encoder_value}") 
                        b_set = False
                    if a_set == False and b_set == False:
                        break 
                if GripA_encoder_value >=target1+1 and GripB_encoder_value>= target1+1:
                    set_servo_speed(A_servo,0)
                    set_servo_speed(B_servo,0)
                    print(f"A : {GripA_encoder_value}")
                    print(f"B : {GripB_encoder_value}")
                    break
            #그리퍼 오픈
            set_servo_angle(A_servo_front, 0)
            set_servo_angle(B_servo_front, 90)
            # 그리퍼 작동
            print("grip stop")
            utime.sleep(2)
    
            GripA_encoder_state = False
            GripB_encoder_state = False

            set_servo_speed(A_servo,100)    #a기준: 100 뒤로
            set_servo_speed(B_servo,-100)   #b기준: -100 뒤로
            # 그리퍼 당기기
            a_set = True
            b_set = True
            while True:
                while True:
                    if  GripA_encoder_value==target2:
                        set_servo_speed(A_servo,0)
                        print(f"A4 : {GripA_encoder_value}")
                        a_set = False
                    if  GripB_encoder_value==target2:
                        set_servo_speed(B_servo,0)
                        print(f"B4 : {GripB_encoder_value}")
                        b_set = False
                    if a_set == False and b_set == False:
                        break
                if GripA_encoder_value <=target2 and GripB_encoder_value<= target2:
                    set_servo_speed(A_servo,0)
                    set_servo_speed(B_servo,0)
                    print(f"A : {GripA_encoder_value}")
                    print(f"B : {GripB_encoder_value}")
                    break

            GripA_encoder_state = True
            GripB_encoder_state = True        
            break
        utime.sleep(3)
        load_state=False
        print("LOAD_complete")

    EV_encorder_state = False
    mortor_down(speed_HI)

    while True:
        if EV_encoder_value == 2:
            EV_encoder_value=0
            motor_stop()
            print(f"EV : {EV_encoder_value}")
            break
    
    set_floor = 0
    STEP_state =2

# 엔코더 인터럽트 설정
EV_encorder_pin.irq(handler=EV_encoder_changed, trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING)
GripA_encoder_pin.irq(handler=GripA_encoder_changed, trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING)
GripB_encoder_pin.irq(handler=GripB_encoder_changed, trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING)

#초기값 설정
motor_stop()
set_servo_speed(A_servo,0)
set_servo_speed(B_servo,0)
set_servo_angle(A_servo_front, 0)
set_servo_angle(B_servo_front, 90)

# 메인 루프
while True:
   #1초마다 엘레베이터 엔코더 벨류 프린트    
    current_time = utime.ticks_ms()
    if utime.ticks_diff(current_time, start_time) >= 1000:
        print("Encoder value:", EV_encoder_value)
        start_time = current_time
    #층수 입력
    if STEP_state== 0: 
        if set_floor == 0:
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
            
    if STEP_state == 2:
        print("done")
        re = input("ok?? :")
        print(f"EV1 : {EV_encoder_value}")
        if re == "ok":
            STEP_state = 0
        utime.sleep(1)
    