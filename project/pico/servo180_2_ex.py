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


def set_servo_angle(servo_pin, angle):
    # 0도: 0.5ms (65535 * 0.5ms / 20ms = 1638)
    # 180도: 2.5ms (65535 * 2.5ms / 20ms = 8191)
    MIN_DUTY = 1638
    MAX_DUTY = 8191
    # 각도를 PWM 신호로 변환하여 서보 모터 각도 설정
    duty = int(MIN_DUTY + (MAX_DUTY - MIN_DUTY) * (angle / 180))
    servo_pin.duty_u16(duty)



# 메인 루프
while True:
    # 서보들을 0도로 회전
        set_servo_angle(A_servo_front, 0)
        set_servo_angle(B_servo_front, 90)

        utime.sleep(2)  # 2초 대기


    # 서보들을 0도로 회전
        set_servo_angle(A_servo_front, 90)
        set_servo_angle(B_servo_front, 0)
        utime.sleep(2)  # 2초 대기


