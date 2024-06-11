from machine import Pin, PWM
import utime

# 서보 모터의 주기 설정 (주파수: 50Hz, 주기: 20ms)
servo_freq = 50
# 서보 모터 핀 설정
A_servo = PWM(Pin(11))
B_servo = PWM(Pin(7))
A_servo_front = PWM(Pin(12))
B_servo_front = PWM(Pin(8))

# 각 서보 모터의 주파수 설정
A_servo.freq(servo_freq)
B_servo.freq(servo_freq)
A_servo_front.freq(servo_freq)
B_servo_front.freq(servo_freq)

load_state = False

GripA_encoder_pin = Pin(10, Pin.IN, Pin.PULL_DOWN)
GripA_encoder_value = 0
GripA_encoder_last_value = 0
GripA_encoder_state = False

GripB_encoder_pin = Pin(6, Pin.IN, Pin.PULL_DOWN)
GripB_encoder_value = 0
GripB_encoder_last_value = 0
GripB_encoder_state = False

def set_servo_angle(servo_pin, angle):
    MIN_DUTY = 1638
    MAX_DUTY = 8191
    duty = int(MIN_DUTY + (MAX_DUTY - MIN_DUTY) * (angle / 180))
    servo_pin.duty_u16(duty)

def GripA_encoder_changed(GripA_encoder_pin):
    global GripA_encoder_value, GripA_encoder_last_value, load_state
    if load_state:
        if GripA_encoder_state and GripA_encoder_last_value == 1 and GripA_encoder_pin.value() == 0:
            GripA_encoder_value += 1
        elif not GripA_encoder_state and GripA_encoder_last_value == 1 and GripA_encoder_pin.value() == 0:
            GripA_encoder_value -= 1
            if GripA_encoder_value < 0:
                GripA_encoder_value = 0
    GripA_encoder_last_value = GripA_encoder_pin.value()

def GripB_encoder_changed(GripB_encoder_pin):
    global GripB_encoder_value, GripB_encoder_last_value, load_state
    if load_state:
        if GripB_encoder_state and GripB_encoder_last_value == 1 and GripB_encoder_pin.value() == 0:
            GripB_encoder_value += 1
        elif not GripB_encoder_state and GripB_encoder_last_value == 1 and GripB_encoder_pin.value() == 0:
            GripB_encoder_value -= 1
            if GripB_encoder_value < 0:
                GripB_encoder_value = 0
    GripB_encoder_last_value = GripB_encoder_pin.value()

def set_servo_speed(servo_pin, speed):
    stop_duty = 4915
    min_duty = 1638
    max_duty = 8191 
    duty = int(stop_duty + (max_duty - stop_duty) * (speed / 100))
    servo_pin.duty_u16(duty)

# 초기값 셋팅
set_servo_speed(A_servo, 0)
set_servo_speed(B_servo, 0)
set_servo_angle(A_servo_front, 0)
set_servo_angle(B_servo_front, 90)

GripA_encoder_pin.irq(handler=GripA_encoder_changed, trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING)
GripB_encoder_pin.irq(handler=GripB_encoder_changed, trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING)

def adjust_motor_speeds(target):
    global GripA_encoder_value, GripB_encoder_value

    while True:
        error_A = target - GripA_encoder_value
        error_B = target - GripB_encoder_value

        if error_A > 0:
            set_servo_speed(A_servo, -100 + error_A)
        else:
            set_servo_speed(A_servo, 0)

        if error_B > 0:
            set_servo_speed(B_servo, 100 + error_B)
        else:
            set_servo_speed(B_servo, 0)

        if GripA_encoder_value >= target and GripB_encoder_value >= target:
            set_servo_speed(A_servo, 0)
            set_servo_speed(B_servo, 0)
            break

def adjust_motor_speeds_reverse(target):
    global GripA_encoder_value, GripB_encoder_value

    while True:
        error_A = target - GripA_encoder_value
        error_B = target - GripB_encoder_value

        if error_A < 0:
            set_servo_speed(A_servo, 100 + error_A)
        else:
            set_servo_speed(A_servo, 0)

        if error_B < 0:
            set_servo_speed(B_servo, -100 + error_B)
        else:
            set_servo_speed(B_servo, 0)

        if GripA_encoder_value <= target and GripB_encoder_value <= target:
            set_servo_speed(A_servo, 0)
            set_servo_speed(B_servo, 0)
            break

def floor_set():
    global GripA_encoder_state, GripB_encoder_state, load_state
    global GripA_encoder_value, GripB_encoder_value

    load_state = True
    print("wait 3 seconds")
    utime.sleep(3)

    while True:
        target_forward = 81
        target_backward = 1
        GripA_encoder_state = True
        GripB_encoder_state = True

        print("grip forward")
        adjust_motor_speeds(target_forward)

        print("grip stop")
        utime.sleep(2)

        set_servo_angle(A_servo_front, 90)
        set_servo_angle(B_servo_front, 0)
        print("grip on")
        utime.sleep(2)

        GripA_encoder_state = False
        GripB_encoder_state = False


        print("grip backward")
        adjust_motor_speeds_reverse(target_backward)

        break

    print("LOAD_complete")

while True:
    if not load_state:
        floor_set()

    print("done")
    utime.sleep(1)