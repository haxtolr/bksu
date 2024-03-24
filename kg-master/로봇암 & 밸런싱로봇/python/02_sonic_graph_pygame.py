import serial
import struct
import pygame
import sys

# 시리얼 포트 설정 (아두이노에서 전송한 시리얼 포트와 동일하게 설정)
SERIAL_PORT = 'COM3'  # 시리얼 포트가 다를 수 있으므로 확인 필요

# 초기화
pygame.init()

# 창 설정
DATA_RANGE = 30
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ultrasonic Sensor Data")

# 데이터 저장용 리스트
distance_data = []

# 시리얼 통신 설정
ser = serial.Serial(SERIAL_PORT, baudrate=9600, timeout=1)

# 텍스트 폰트 설정
font = pygame.font.SysFont(None, 24)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:  # q 키를 누르면 종료
                running = False

    # 시리얼 데이터 읽기
    if ser.in_waiting >= 4:  # 4바이트를 기준으로 읽어옴 (long 자료형의 크기)
        data = ser.read(4)
        distance = struct.unpack('l', data)[0]  # 바이트를 long 형으로 언패킹
        distance_data.append(distance)

        # 그래프 그리기
        screen.fill((0, 0, 0))  # 화면을 검은색으로 채우기
        if len(distance_data) >= 2:
            for i in range(len(distance_data) - 1):
                # x 좌표 계산 (일정한 간격으로)
                x1 = i * (SCREEN_WIDTH - 40) / len(distance_data) + 20  # 시작점의 x 좌표 (20은 왼쪽 여백)
                x2 = (i + 1) * (SCREEN_WIDTH - 40) / len(distance_data) + 20  # 끝점의 x 좌표 (20은 왼쪽 여백)
                # y 좌표 계산 (데이터의 범위에 따라 조정)
                y1 = SCREEN_HEIGHT - (distance_data[i] * (SCREEN_HEIGHT - 40) / DATA_RANGE) + 20
                y2 = SCREEN_HEIGHT - (distance_data[i + 1] * (SCREEN_HEIGHT - 40) / DATA_RANGE) + 20
                pygame.draw.line(screen, (255, 255, 255), (x1, y1), (x2, y2), 2)

        # 텍스트 그리기 (x축 라벨)
        x_label = font.render('Time', True, (255, 255, 255))
        x_label_pos = (SCREEN_WIDTH // 2 - x_label.get_width() // 2, SCREEN_HEIGHT - 20)  # 화면의 중앙 아래에 표시
        screen.blit(x_label, x_label_pos)
        
        # 텍스트 그리기 (y축 라벨)
        y_label = font.render('Distance (cm)', True, (255, 255, 255))
        y_label = pygame.transform.rotate(y_label, 90)  # 텍스트를 세로로 회전
        y_label_pos = (5, SCREEN_HEIGHT // 2 - y_label.get_height() // 2)  # 화면의 왼쪽 중앙에 표시
        screen.blit(y_label, y_label_pos)

        # 텍스트 그리기 (거리 정보)
        text = font.render(f'Distance: {distance} cm', True, (255, 0, 0))
        text_pos = (SCREEN_WIDTH // 2 - text.get_width() // 2, 10)  # 화면의 상단 중앙에 표시
        screen.blit(text, text_pos)

        pygame.display.flip()

# 시리얼 포트 닫기
ser.close()
pygame.quit()
sys.exit()



        # # 텍스트 그리기 (x축 라벨)
        # x_label = font.render('Time', True, (255, 255, 255))
        # screen.blit(x_label, (SCREEN_WIDTH // 2 - x_label.get_width() // 2, SCREEN_HEIGHT - 20))  # 아래쪽 중앙에 표시

        # # 텍스트 그리기 (y축 라벨)
        # y_label = font.render('Distance (cm)', True, (255, 255, 255))
        # y_label = pygame.transform.rotate(y_label, 90)  # 텍스트를 세로로 회전
        # screen.blit(y_label, (5, SCREEN_HEIGHT // 2 - y_label.get_height() // 2))  # 왼쪽 중앙에 표시

        # # 텍스트 그리기
        # text = font.render(f'Distance: {distance} cm', True, (255, 0, 0))
        # screen.blit(text, (SCREEN_WIDTH//2-text.get_width()//2, 10))  # 텍스트의 위치를 조정하여 위쪽 여백에 표시
                
