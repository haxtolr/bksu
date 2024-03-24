import cv2
import mediapipe as mp
import numpy as np
import serial
import math

ser = serial.Serial("COM3", 115200)

mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

def calculate_angle(a, b, c):
    radians = math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0])
    angle = np.degrees(radians)
    if angle < 0:
        angle += 360
    return angle

def main():
    counter = 0
    arm_down = True
    isMoveDone = True

    cap = cv2.VideoCapture(0)
    cap.set(3, 640) # Set the width
    cap.set(4, 480) # Set the height

    while cap.isOpened():
        ret, image = cap.read()
        if not ret:
            break

        image_height, image_width, _ = image.shape
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = pose.process(image_rgb)

        if results.pose_landmarks is not None:
            landmarks = results.pose_landmarks.landmark
            
            # Get the image pixel coordinates of each joint
            wrist = (int(landmarks[mp_pose.PoseLandmark.RIGHT_WRIST].x * image_width), 
                     int(landmarks[mp_pose.PoseLandmark.RIGHT_WRIST].y * image_height))
            elbow = (int(landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW].x * image_width), 
                     int(landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW].y * image_height))
            shoulder = (int(landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER].x * image_width), 
                        int(landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER].y * image_height))
            right_hip = (int(landmarks[mp_pose.PoseLandmark.RIGHT_HIP].x * image_width), 
                         int(landmarks[mp_pose.PoseLandmark.RIGHT_HIP].y * image_height))
            right_thumb = (int(landmarks[mp_pose.PoseLandmark.RIGHT_THUMB].x * image_width), 
                           int(landmarks[mp_pose.PoseLandmark.RIGHT_THUMB].y * image_height))

            # Calculate the angles
            angle_wrist = calculate_angle(right_thumb, wrist, elbow)
            angle_elbow = calculate_angle(wrist, elbow, shoulder)
            angle_shoulder = calculate_angle(elbow, shoulder, right_hip)

            # Visualize the joints
            cv2.circle(image, wrist, 10, (255,0,0), -1)
            cv2.circle(image, elbow, 10, (0,255,0), -1)
            cv2.circle(image, shoulder, 10, (0,0,255), -1)             
            cv2.line(image, shoulder, elbow, (255,255,0), 3)
            cv2.line(image, elbow, wrist, (0,255,255), 3)

            # Display the angles
            cv2.putText(image, f'Angle Shoulder: {round(angle_shoulder, 2)}', (elbow[0], elbow[1] + 20), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
            cv2.putText(image, f'Angle Elbow: {round(angle_elbow, 2)}', (elbow[0], elbow[1] + 40), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
            cv2.putText(image, f'Angle Wrist: {round(angle_wrist, 2)}', (elbow[0], elbow[1] + 60), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

            # Count and display
            angle = calculate_angle(shoulder, elbow, wrist)
            if angle <= 45 and not arm_down:
                counter += 1
                arm_down = True
            if angle > 45:
                arm_down = False
            cv2.putText(image, f'Count: {counter}', (10, 50), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

            # Serial communication
            command = f"90,{int(angle_shoulder)},{int(angle_elbow)},{int(angle_wrist)}d"
            command_bytes = command.encode('utf-8')
            if isMoveDone:
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
        
        cv2.imshow('Mediapipe Feed', image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    ser.close()
    cap.release()
	cv2.destroyAllWindows()  # 이 위치에 배치

if __name__ == "__main__":
    main()