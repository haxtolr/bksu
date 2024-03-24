# 팔이 접히는 각도 구하기

import cv2
import mediapipe as mp
import numpy as np
import serial

ser = serial.Serial("COM3", 115200)

def calculate_angle(a,b,c):
    a = np.array(a) # First
    b = np.array(b) # Mid
    c = np.array(c) # End
    
    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians*180.0/np.pi)
    
    if angle > 180.0:
        angle = 360-angle
        
    return angle

counter = 0
arm_down = True

cap = cv2.VideoCapture(0)
cap.set(3, 640) # 화면 넓이 설정
cap.set(4, 480) # 화면 높이 설정

mp_pose = mp.solutions.pose # 이미지 추정모델을 mp_pose 로 가져오기
pose = mp_pose.Pose() # 포즈 추정모델을 pose 객체로 생성

isMoveDone = True

with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, image = cap.read()
        image_height, image_width, _ = image.shape
        
        # 포즈 모델을 사용하여 이미지에서 포즈를 예측하고, 결과를 results 변수에 저장
        results = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)) 
        
        try:
            landmarks = results.pose_landmarks.landmark
            
            # 각 관절의 위치점 찾기
            shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
            elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
            wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
            
            shoulder_pos = tuple(np.multiply(shoulder, [image_width, image_height]).astype(int))
            elbow_pos = tuple(np.multiply(elbow, [image_width, image_height]).astype(int))
            wrist_pos = tuple(np.multiply(wrist, [image_width, image_height]).astype(int))  
            
                            
            # 포인트 비주얼 처리
            
            cv2.circle(image, shoulder_pos, 10, (255,0,0), -1)
            cv2.circle(image, elbow_pos, 10, (0,255,0), -1)
            cv2.circle(image, wrist_pos, 10, (0,0,255), -1)             
            cv2.line(image, shoulder_pos, elbow_pos,   (255,255,0), 3)
            cv2.line(image, elbow_pos, wrist_pos, (0,255,255), 3)
            
                
            # 각도 계산하기
            angle = calculate_angle(shoulder, elbow, wrist)
            
            # 각도 표시하기
            cv2.putText(image, f'Angle: {round(angle, 2)}', (elbow_pos[0], elbow_pos[1]), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
            

            image = cv2.flip(image, 1)
            
            if angle <= 45 and not arm_down:
                counter += 1
                arm_down = True
            
            if angle > 45:
                arm_down = False
            
            cv2.putText(image, f'Count: {counter}', (10, 50), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

            command = f"90,90,{int(angle)},90d"
            command_bytes = command.encode('utf-8')
            
            if (isMoveDone):
                ser.write(command_bytes)
                print(command)
                isMoveDone = False
            else:
                print("skip")
                
            if ser.read() == b'd':
                print("process done")
                isMoveDone = True
            else:
                print('wait')
            
            key = cv2.waitKey(10) # 키 입력 확인
            if key == ord('q') or key == 27:  # 'q' 키 또는 ESC 키를 입력하면 종료
                break
            
        except Exception as e:
            print(e)
            pass  
    
        cv2.imshow('Mediapipe Feed', image)   
    
    
    command = f"90,90,90,90d"
    command_bytes = command.encode('utf-8')   
    ser.write(command_bytes)
    
    ser.close()
    cap.release()
    cv2.destroyAllWindows()