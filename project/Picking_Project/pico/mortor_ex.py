from machine import Pin, PWM
import time

# PWM 핀 설정
enB = PWM(Pin(20))  # GPIO 15번 핀을 PWM 핀으로 사용
enB.freq(1000)  # PWM 주파수를 1kHz로 설정
in3 = Pin(18, Pin.OUT)  # 방향 제어 핀 1 
in4 = Pin(19, Pin.OUT)  # 방향 제어 핀 2 

def motor_down():
    in3.high()
    in4.low()

def motor_up():
    in3.low()
    in4.high()

def motor_stop():
    in3.low()
    in4.low()

def set_motor_speed(duty_cycle):
    enB.duty_u16(duty_cycle)

def main():
    while True:
        # 모터 속도 제어 (0-65535 사이 값)
        motor_up()
        set_motor_speed(32768)  # 모터를 중간 속도로 회전

        # 2초 동안 대기
        time.sleep(1)

        # 모터 속도 증가
        motor_down()
        set_motor_speed(10000)  # 모터를 최대 속도로 회전

        # 2초 동안 대기
        time.sleep(1)

        # 모터 속도 감소
        set_motor_speed(0)  # 모터를 정지

        # 2초 동안 대기
        time.sleep(2)

if __name__ == "__main__":
    main()