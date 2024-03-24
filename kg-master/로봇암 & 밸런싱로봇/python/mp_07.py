import cv2
import mediapipe as mp
import numpy as np
import serial

ser = serial.Serial('COM3', 115200, timeout=0.5)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

bar_x, bar_y, bar_width, bar_height = 500, 50, 20, 255
bar_max_color = (0, 255, 0)
max_distance = 200
led_bright_max = 255

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        hand_landmarks = results.multi_hand_landmarks[0]
        thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
        index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]

        img_height, img_width, _ = frame.shape
        thumb_x, thumb_y = int(thumb_tip.x * img_width), int(thumb_tip.y * img_height)
        index_x, index_y = int(index_tip.x * img_width), int(index_tip.y * img_height)

        distance = ((index_x - thumb_x) ** 2 + (index_y - thumb_y) ** 2) ** 0.5
    
        led_brightness = int((distance / max_distance) * led_bright_max)
        bar_color = tuple(np.multiply(bar_max_color, led_brightness / led_bright_max).astype(int))

        # 손가락 거리에 따라 슬라이드바 표시하기
        cv2.rectangle(frame, (bar_x, bar_y), (bar_x + bar_width, bar_y + bar_height), (255, 255, 255), -1)  # Clear the rectangle
        cv2.rectangle(frame, (bar_x, bar_y + bar_height - led_brightness), (bar_x + bar_width, bar_y + bar_height), tuple(map(int, bar_color)), -1)  # Fill the rectangle

        cv2.circle(frame, (thumb_x, thumb_y), 5, (0, 255, 0), -1)  # Green circle on thumb
        cv2.circle(frame, (index_x, index_y), 5, (0, 255, 0), -1)  # Green circle on index finger
        ser.write(led_brightness.to_bytes(1, 'big'))
      
    cv2.imshow('Hand Landmarks', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()