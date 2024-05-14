from pymycobot.mycobot import MyCobot
import cv2
import time

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


while True:
    ret, frame = cap.read()

    width = frame.shape[1]


    # 왼쪽과 오른쪽으로 약 10% 정도 프레임을 잘라낸다.
    cropped_frame = frame[:, int(width*0.1):int(width*0.9)]


    cv2.imshow('frame', cropped_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()