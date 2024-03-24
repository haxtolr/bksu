import mediapipe as mp
import numpy as np
import cv2

def calulate_angle(a, b, c):
	a = np.array(a)
	b = np.array(b)
	c = np.array(c)

	radian = np.arccos((np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])))
	angle = np.abs(radian * 180.0 / np.pi)

	if angle > 180.0:
		angle = 360 - angle
	return angle


cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

mp_pose = mp.solutions.pose

# Pose 객체를 생성하고 최소 탐지 신뢰도와 최소 추적 신뢰도를 설정합니다.
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
	while cap.isOpened():
		ret, image = cap.read()
		image_h, image_w, _ = image.shape

		# 이미지를 RGB 형식으로 변환하고 Pose 객체를 통해 처리합니다.
		result = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
		
		if result.pose_landmarks:
			# 왼쪽 어깨의 위치를 가져옵니다.
			left_shoulder = result.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER]
			shoulder_pos = (int(left_shoulder.x * image_w), int(left_shoulder.y * image_h))
			elbow_pos = (int(result.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW].x * image_w), int(result.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW].y * image_h))
			wrist_pos = (int(result.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST].x * image_w), int(result.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST].y * image_h))

			print(shoulder_pos)
			# 어깨, 팔꿈치, 손목 위치에 원을 그립니다.
			cv2.circle(image, shoulder_pos, 5, (0, 0, 255), -1)
			cv2.circle(image, elbow_pos, 5, (0, 0, 255), -1)
			cv2.circle(image, wrist_pos, 5, (0, 0, 255), -1)
			cv2.line(image, shoulder_pos, elbow_pos, (255, 0, 255), 3)
			cv2.line(image, elbow_pos, wrist_pos, (255, 255, 255), 3)
			
			angle = calulate_angle(shoulder_pos, elbow_pos, wrist_pos)
			cv2.putText(image, f"Angle: {int(angle)}", (20, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

			cv2.imshow("cam", image)
			
			ky = cv2.waitKey(10)
			if (ky == ord('q') or ky == 27):
				break

cap.release()
cap.destroyAllWindows()
