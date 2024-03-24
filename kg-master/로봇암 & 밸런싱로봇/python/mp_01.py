import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

while cap.isOpened():
	ret, image = cap.read()
	cv2.imshow("cam", image)

	ky = cv2.waitKey(0)
	if (ky == ord('q') or ky == 27):
		break

cap.release()
cv2.destroyAllWindows()