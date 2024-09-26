from machine import Pin, PWM
import utime


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


load_state=False

GripA_encoder_pin = Pin(10, Pin.IN, Pin.PULL_DOWN)
GripA_encoder_value = 0
GripA_encorder_last_value = 0
GripA_encoder_state = False #true-> 증가방향 false-> 감소방향

GripB_encoder_pin = Pin(6, Pin.IN, Pin.PULL_DOWN)
GripB_encoder_value = 0
GripB_encorder_last_value = 0
GripB_encoder_state = False

def set_servo_angle(servo_pin, angle):
    # 0도: 0.5ms (65535 * 0.5ms / 20ms = 1638)
    # 180도: 2.5ms (65535 * 2.5ms / 20ms = 8191)
    MIN_DUTY = 1638
    MAX_DUTY = 8191
    # 각도를 PWM 신호로 변환하여 서보 모터 각도 설정
    duty = int(MIN_DUTY + (MAX_DUTY - MIN_DUTY) * (angle / 180))
    servo_pin.duty_u16(duty)

def GripA_encoder_changed(GripA_encoder_pin):
    global GripA_encoder_value, GripA_encorder_last_value,load_state
    
    if load_state: 
        if  GripA_encoder_state and GripA_encorder_last_value == 1 and GripA_encoder_pin.value() == 0:
            GripA_encoder_value += 1
            print("a_Encoder value changed:", GripA_encoder_value)
        elif not GripA_encoder_state and GripA_encorder_last_value == 1 and GripA_encoder_pin.value() == 0:
            GripA_encoder_value -= 1
            print("a_Encoder value changed:", GripA_encoder_value)
            if GripA_encoder_value < 0:
                GripA_encoder_value = 0
                print("a_NOT INPUT", GripA_encoder_value)
       
    GripA_encorder_last_value = GripA_encoder_pin.value()

def GripB_encoder_changed(GripB_encoder_pin):
    global GripB_encoder_value, GripB_encorder_last_value,load_state
    if load_state:
        if GripB_encoder_state and GripB_encorder_last_value == 1 and GripB_encoder_pin.value() == 0:
            GripB_encoder_value += 1
            print("B_Encoder value changed:", GripB_encoder_value)
        elif not GripB_encoder_state and GripB_encorder_last_value == 1 and GripB_encoder_pin.value() == 0:
            GripB_encoder_value -= 1
            print("B_Encoder value changed:", GripB_encoder_value)
            if GripB_encoder_value < 0:
                GripB_encoder_value = 0
                print("B_NOT INPUT", GripB_encoder_value)

    GripB_encorder_last_value = GripB_encoder_pin.value()




def set_servo_speed(servo_pin, speed):
    # 0도: 0.5ms (65535 * 0.5ms / 20ms = 1638)
    # 180도: 2.5ms (65535 * 2.5ms / 20ms = 8191)
 
    stop_duty = 4915
    min_duty = 1638
    max_duty = 8191 

    duty = int(stop_duty + (max_duty - stop_duty) * (speed / 100))
    servo_pin.duty_u16(duty)
#초기값 셋팅
set_servo_speed(A_servo,0)
set_servo_speed(B_servo,0)
set_servo_angle(A_servo_front, 0)
set_servo_angle(B_servo_front, 90)
GripA_encoder_pin.irq(handler=GripA_encoder_changed, trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING)
GripB_encoder_pin.irq(handler=GripB_encoder_changed, trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING)

# 메인 루프




def floor_set():
    
    #global set_floor,EV_encorder_state,EV_encoder_value
    global GripA_encoder_state,GripB_encoder_state ,load_state
    global GripA_encoder_value,GripB_encoder_value
 
    #motor_stop()
    #print(f"{set_floor}: floor")
    load_state=True
    print("wait 3 seconds")  
    utime.sleep(3) # 작업

    while True:
        target1=81
        target2=1
        GripA_encoder_state = True
        GripB_encoder_state = True

        set_servo_speed(A_servo,-100)   #a기준: -100 앞으로
        set_servo_speed(B_servo,100)  #b기준: 100 앞으로
        print("girp _forward")

        while True:
            
            if  GripA_encoder_value>=target1:
                set_servo_speed(A_servo,0)
            if  GripB_encoder_value>=target1:
                set_servo_speed(B_servo,0)
            if GripA_encoder_value >=target1+1 and GripB_encoder_value>= target1+1:
                set_servo_speed(A_servo,0)
                set_servo_speed(B_servo,0)
                break


    
        print("grip stop")
        utime.sleep(2)
    
        #서보들을 0도로 회전
        set_servo_angle(A_servo_front, 90)
        set_servo_angle(B_servo_front, 0)
        print("girp on")
        utime.sleep(2)  # 2초 대기

        GripA_encoder_state = False
        GripB_encoder_state = False

        set_servo_speed(A_servo,100)    #a기준: 100 뒤로
        set_servo_speed(B_servo,-100)   #b기준: -100 뒤로

        while True:
           
            if  GripA_encoder_value<=target2+1:
                set_servo_speed(A_servo,0)
            if  GripB_encoder_value<=target2+1:
                set_servo_speed(B_servo,0)
            if GripA_encoder_value <=target2 and GripB_encoder_value<= target2:
                set_servo_speed(A_servo,0)
                set_servo_speed(B_servo,0)
                break


        break
    
        print("LOAD_complete")

        #EV_encorder_state = False
        #mortor_down(speed_HI)

    # while True:
    #     if EV_encoder_value ==3:
    #         motor_stop()
    #         break
    
        #set_floor = 0
        floor_set_DONE =True
    

    

while True:

    if not load_state:
        floor_set()

    print("done")
    utime.sleep(1)
