import serial
import struct
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 시리얼 포트 설정 (아두이노에서 전송한 시리얼 포트와 동일하게 설정)
SERIAL_PORT = 'COM3'  # 시리얼 포트가 다를 수 있으므로 확인 필요

# 데이터 저장용 리스트
distance_data = []

# 시리얼 통신 설정
ser = serial.Serial(SERIAL_PORT, baudrate=9600, timeout=1)

# 그래프 초기 설정
fig, ax = plt.subplots()
line, = ax.plot([], [])
ax.set_xlim(0, 100)
ax.set_ylim(0, 35)
ax.set_xlabel('Time')
ax.set_ylabel('Distance (cm)')
ax.set_title('Ultrasonic Sensor Data')
text = ax.text(10, 30, '', fontsize=12, color='red')

def update(frame):
    if ser.in_waiting >= 4:  # 4바이트를 기준으로 읽어옴 (long 자료형의 크기)
        data = ser.read(4)
        distance = struct.unpack('l', data)[0]  # 바이트를 long 형으로 언패킹
        distance_data.append(distance)

        # 새로운 데이터를 플로팅
        line.set_data(range(len(distance_data)), distance_data)
        text.set_text(f'Distance: {distance} cm')

ani = FuncAnimation(fig, update, frames=None, blit=False, interval=50)

# 키보드 이벤트 처리
def on_key(event):
    if event.key == 'q':
        plt.close()
        ser.close()

cid = fig.canvas.mpl_connect('key_press_event', on_key)

plt.show()
