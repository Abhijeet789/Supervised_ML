#This is a program to take a snap from the web cam and copy a section of that snap and paste it on another image

#importing libraries 
import cv2

#loading the image
img = cv2.imread("dog.jpg")

#starting the camera
capture = cv2.VideoCapture(0)

#cheching the status of the camera
while capture.isOpened() :
	print("\nThe camera is ready to take the picture ")
	#taking the input from the user that whenever he is ready to tale the picture
	print("\nPress Y to capture the picture when you are ready " )
	status,frame = capture.read()
	cv2.rectangle(frame,(300,150),(500,350),(0,255,0),2)
	cv2.imshow("frame1",frame)
	
	if cv2.waitKey(1) & 0xFF == ord('y') :
		#taking the image			
		status,frame = capture.read()

		#saving and copying the part of captured image into roi(region of interest)
		roi = frame[150:350 , 300 :500]         #coordinates of the rectangle form are (100,200) and (250,350)

		#printing the shape of copied part i.e, roi
		print(roi.shape)

		#cheching the shape of an image onto which copied part is to be pasted
		print(img.shape)
	
		#printing the number of rows of the copied part
		print(roi.shape[0])

		#printing the number of coloumns of the copied part
		print(roi.shape[1])

		#pasting the copied part onto another image with starting co-ordinate (10,20) 
		img[100:roi.shape[0]+100 , 800:roi.shape[1]+800]=roi

		#displaying the captured image from which a part is copied
		cv2.imshow('img1', frame)

		#displaying the copied part
		cv2.imshow('roi', roi)

		#displaying the image on which a part is pasted
		cv2.imshow('img', img)

		#closing the camera by release function	
		capture.release()
		#holding the screen to display the image for infinite time
		cv2.waitKey(0)
		#to close all windows		
		if cv2.waitKey(1) & 0xFF==ord('q'):			
			cv2.destroyAllWindows()
			break
				
		

	else:	
		print("\nYou have entered a wrong input ")
	



