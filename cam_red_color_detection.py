#This is a python3 program used to highlight only red color in the camera frame

#importing libraries
import cv2

cap = cv2.VideoCapture(0)

while cap.isOpened():
	#print("\nThe camera is ready to take the picture " )
	#taking the picture
	status,frame = cap.read()
	#highlighting the red region
	onlyred = cv2.inRange(frame,(0,0,100),(40,40,255))
	cv2.imshow("red",onlyred)
	if cv2.waitKey(1) & 0xFF == ord("q"):
		break

#releasing the camera
cap.release()
cv2.destroyAllWindows()
	
