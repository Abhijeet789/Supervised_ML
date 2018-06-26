#This is a python3 program which is to detect the motion infront of the webcam

#importing the libraries
import cv2

#declaring the function to process on gthe frame and to calculate the difference in frames
def img_dif(x,y,z):
	img1 = cv2.absdiff(x,y)
	img2 = cv2.absdiff(y,z)
	dif = cv2.bitwise_and(img1,img2)
	print(dif)
	return dif

#opening the camera
capture = cv2.VideoCapture(0)

#taking the three continuous frames 
frame1 = capture.read()[1]
frame2 = capture.read()[1]
frame3 = capture.read()[1]

#converting the captured frames into black and white format
gray1 = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)
gray3 = cv2.cvtColor(frame3,cv2.COLOR_BGR2GRAY)

#taking the loop to detect the motion in the frames
while capture.isOpened():
	#passing the captured frames as the argument of the function img_dif	
	img_motion = img_dif(gray1,gray2,gray3)
	#displaying the motion 
	cv2.imshow("motion",img_motion)
	#capturing the new frame
	status , frame = capture.read()
	#to detect the motion, comparing three new frames
	gray1 = gray2
	gray2 = gray3
	gray3 = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	
	#holding the frame and exiting from the program when q is pressed
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

#releasing the camera
capture.release()
#closing all the windows
cv2.destroyAllWindows()
