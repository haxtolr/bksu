from machine import Pin, PWM
import utime

# 서보 모터 핀 설정
servo_pin = PWM(Pin(7))  # GPIO 10번 핀을 PWM 핀으로 사용

#servo_pin = PWM(Pin(11))  # GPIO 15번 핀을 PWM 핀으로 사용

# 서보 모터의 주기 설정 (주파수: 50Hz, 주기: 20ms)
servo_pin.freq(50)

def set_servo_speed(speed):
    # 0도: 0.5ms (65535 * 0.5ms / 20ms = 1638)
    # 180도: 2.5ms (65535 * 2.5ms / 20ms = 8191)
 
    stop_duty = 4915
    min_duty = 1638
    max_duty = 8191 

    duty = int(stop_duty + (max_duty - stop_duty) * (speed / 100))

    servo_pin.duty_u16(duty)


# 메인 루프
while True:
    # 한 방향으로 점점 빠르게 회전하는 예제
    set_servo_speed(100)
    print("a")
    utime.sleep(3)
    set_servo_speed(0)
    print("b")
    utime.sleep(2) 
    # 정지
    set_servo_speed(-100)
    print("c")
    utime.sleep(3) 
    set_servo_speed(0)
    print("b")
   
    utime.sleep(2)  # 2초 대기
