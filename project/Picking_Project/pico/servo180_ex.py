from machine import Pin, PWM
import utime

# 서보 모터 핀 설정
servo_pin = PWM(Pin(11))  # GPIO 11번 핀을 PWM 핀으로 사용

# 서보 모터의 주기 설정 (주파수: 50Hz, 주기: 20ms)
servo_pin.freq(50)

def set_servo_angle(angle):
    # 각도를 PWM 신호로 변환하여 서보 모터 각도 설정
    # 0도: 0.5ms (65535 * 0.5ms / 20ms = 1638)
    # 180도: 2.5ms (65535 * 2.5ms / 20ms = 8191)
    min_duty = 1638
    max_duty = 8191
    duty = int(min_duty + (max_duty - min_duty) * (angle / 180))
    servo_pin.duty_u16(duty)
# 메인 루프
while True:
    # 0도에서 180도까지 10도씩 회전하는 예제
        set_servo_angle(180)
        utime.sleep(2)  # 0.5초 대기
        set_servo_angle(0)
        utime.sleep(2)  # 0.5초 대기
        
        

   