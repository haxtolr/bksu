import machine
import utime
import time
import sys

motor_pin_down = machine.Pin(18, machine.Pin.OUT)
motor_pin_up = machine.Pin(19, machine.Pin.OUT)

# 엔코더 핀 설정
encoder_pin = machine.Pin(20, machine.Pin.IN, machine.Pin.PULL_DOWN)

# 버튼 핀 설정
button_pin = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)

# 전역 변수 선언
encoder_value = 0
encoder_last_value = 0
encoder_state = True
# 엔코더 핀 변경 감지 함수
def encoder_changed(encoder_pin):
    global encoder_value, encoder_last_value
    
    if encoder_state and encoder_last_value == 1 and encoder_pin.value() == 0:
        encoder_value += 1
        print("Encoder value changed:", encoder_value)
    elif not encoder_state and encoder_last_value == 1 and encoder_pin.value() == 0:
        encoder_value -= 1
        if encoder_value < 0:
              encoder_value = 0
        print("Encoder value changed:", encoder_value)
    encoder_last_value = encoder_pin.value()

# 버튼 핀 변경 감지 함수
def button_pressed(button_pin):
    global encoder_value
    
    encoder_value = 0
    motor_pin_down.value(0)
    motor_pin_up.value(0)
    print("Button pressed, encoder value reset to 0")

def floor_set():
	global set_floor
	global encoder_state
	global encoder_value

	motor_pin_up.value(0)
	print(f"{set_floor}: floor")
	time.sleep(3) # 작업 
	print("wait 3 seconds")
	encoder_state = False
	motor_pin_down.value(0)
	if encoder_value == 0:
		motor_pin_down.value(1)
		print("0 floor, end")
	set_floor = 0
        
            

# 엔코더 인터럽트 설정
encoder_pin.irq(handler=encoder_changed, trigger=machine.Pin.IRQ_RISING | machine.Pin.IRQ_FALLING)

# 버튼 인터럽트 설정
button_pin.irq(handler=button_pressed, trigger=machine.Pin.IRQ_FALLING)

# 층수 입력
set_floor = int(input("Set the floor: "))


# 메인 루프
while True:
    utime.sleep(1)  # 1초마다 출력 확인
    print("Encoder value:", encoder_value)
    motor_pin_up.value(1)
    if set_floor == 1:
          if encoder_value >= 10 and encoder_value < 15:
                floor_set()
    elif set_floor == 2:
          if encoder_value >= 20 and encoder_value < 25:
                floor_set()
    elif set_floor == 3:
         if encoder_value >= 30 and encoder_value < 35:
                floor_set()