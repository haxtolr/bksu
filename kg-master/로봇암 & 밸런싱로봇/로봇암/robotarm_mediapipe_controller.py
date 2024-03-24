import cv2 as cv
import mediapipe as mp
import numpy as np
import serial
import time
import math

class RobotArmController:
    def __init__(self, port, baudrate):
        if not (hasattr(self, 'ser') and self.ser.is_open):
            self.ser = serial.Serial(port, baudrate)


        self.mp_pose = mp.solutions.pose
        self.mp_drawing = mp.solutions.drawing_utils

    def calculate_angle_2x(self, a, b):
        angle_rad = math.atan2(b.y - a.y, b.x - a.x)
        angle_deg = math.degrees(angle_rad)
        return angle_deg

    def calculate_angle(self, a, b, c):
        a = np.array(a)
        b = np.array(b)
        c = np.array(c)

        radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - \
            np.arctan2(a[1] - b[1], a[0] - b[0])
        angle = np.abs(radians * 180.0 / np.pi)

        if angle > 180.0:
            angle = 360 - angle

        return angle

    def detection_body_part(self, landmarks, body_part_name):
        return [
            landmarks[self.mp_pose.PoseLandmark[body_part_name].value].x,
            landmarks[self.mp_pose.PoseLandmark[body_part_name].value].y,
            landmarks[self.mp_pose.PoseLandmark[body_part_name].value].visibility
        ]

    def angle_of_the_RIGHT_arm(self, landmarks):
        R_shoulder = self.detection_body_part(landmarks, 'RIGHT_SHOULDER')
        R_elbow = self.detection_body_part(landmarks, 'RIGHT_ELBOW')
        R_wrist = self.detection_body_part(landmarks, 'RIGHT_WRIST')
        return self.calculate_angle(R_shoulder, R_elbow, R_wrist)

    def angle_of_the_RIGHT_wrist(self, landmarks):
        R_elbow = self.detection_body_part(landmarks, 'RIGHT_ELBOW')
        R_wrist = self.detection_body_part(landmarks, 'RIGHT_WRIST')
        R_thumb = self.detection_body_part(landmarks, 'RIGHT_THUMB')
        return self.calculate_angle(R_elbow, R_wrist, R_thumb)

    def run(self):
        pose = self.mp_pose.Pose(static_image_mode=False, enable_segmentation=True, min_detection_confidence=0.5, min_tracking_confidence=0.5)

        cap = cv.VideoCapture(0, cv.CAP_DSHOW)

        desired_ratio = 16 / 9
        new_width = 1280  
        new_height = int(new_width / desired_ratio)  
        cap.set(cv.CAP_PROP_FRAME_WIDTH, new_width)
        cap.set(cv.CAP_PROP_FRAME_HEIGHT, new_height)

        isMoveDone = True

        while True:
            ret, frame = cap.read()
            if not ret:
                print('프레임 획득에 실패하여 루프를 나갑니다.')
                break

            frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

            frame.flags.writeable = False
            res = pose.process(frame)
            frame.flags.writeable = True

            if res and res.pose_landmarks:

                landmarks = res.pose_landmarks.landmark

                myAngleArm3 = self.angle_of_the_RIGHT_arm(landmarks) - 90
                if (myAngleArm3 < 0):
                    myAngleArm3 = 10

                myAngleWrist3 = self.angle_of_the_RIGHT_wrist(landmarks)

                myAngleShoulder = abs(self.calculate_angle_2x(landmarks[self.mp_pose.PoseLandmark['RIGHT_SHOULDER']], landmarks[self.mp_pose.PoseLandmark['RIGHT_ELBOW']]))
                myAngleArm = abs(self.calculate_angle_2x(landmarks[self.mp_pose.PoseLandmark['RIGHT_ELBOW']], landmarks[self.mp_pose.PoseLandmark['RIGHT_WRIST']]))
                myAngleWrist = abs(self.calculate_angle_2x(landmarks[self.mp_pose.PoseLandmark['RIGHT_WRIST']], landmarks[self.mp_pose.PoseLandmark['RIGHT_THUMB']]))

                for landmark in [self.mp_pose.PoseLandmark.RIGHT_SHOULDER, self.mp_pose.PoseLandmark.RIGHT_ELBOW, self.mp_pose.PoseLandmark.RIGHT_WRIST, self.mp_pose.PoseLandmark.RIGHT_THUMB]:
                    landmark_point = res.pose_landmarks.landmark[landmark.value]
                    landmark_px = int(landmark_point.x * frame.shape[1])
                    landmark_py = int(landmark_point.y * frame.shape[0])
                    cv.circle(frame, (landmark_px, landmark_py), 5, (0, 255, 0), -1)

                for connection in [(self.mp_pose.PoseLandmark.RIGHT_SHOULDER, self.mp_pose.PoseLandmark.RIGHT_ELBOW),
                                (self.mp_pose.PoseLandmark.RIGHT_ELBOW, self.mp_pose.PoseLandmark.RIGHT_WRIST),
                                (self.mp_pose.PoseLandmark.RIGHT_WRIST, self.mp_pose.PoseLandmark.RIGHT_THUMB)]:
                    point1 = res.pose_landmarks.landmark[connection[0].value]
                    point2 = res.pose_landmarks.landmark[connection[1].value]
                    point1_px = (int(point1.x * frame.shape[1]), int(point1.y * frame.shape[0]))
                    point2_px = (int(point2.x * frame.shape[1]), int(point2.y * frame.shape[0]))
                    cv.line(frame, point1_px, point2_px, (0, 255, 0), 2)

                frame = cv.flip(frame, 1)

                cv.putText(frame, f"Angle Wrist: {round(myAngleWrist, 2)}", (50, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2, cv.LINE_AA)
                cv.putText(frame, f"Angle Arm3: {round(myAngleArm3, 2)}", (50, 100), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv.LINE_AA)
                cv.putText(frame, f"Angle Shoulder: {round(myAngleShoulder, 2)}", (50, 150), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA)

                cv.imshow('MediaPipe pose', frame)

                command = f"90,{int(myAngleShoulder)},{int(myAngleArm3)},{int(myAngleWrist)}d"
                command_bytes = command.encode('utf-8')

                if (isMoveDone):
                    self.ser.write(command_bytes)
                    print(command)
                    isMoveDone = False

                if self.ser.read() == b'd':
                    print('process')
                    isMoveDone = True
                else:
                    print('wait')

                if cv.waitKey(1) in (ord('q'), ord('Q'), 27):  # q 또는 Q 또는 ESC 누르면 종료
                    break

        command = f"90,90,90,90d"
        command_bytes = command.encode('utf-8')
        self.ser.write(command_bytes)

        self.ser.close()
        cap.release()
        cv.destroyAllWindows()
