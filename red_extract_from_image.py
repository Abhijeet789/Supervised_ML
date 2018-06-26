#This is a program to extractt only red color from the image

#loading the libraries
import cv2

#loading the image
img = cv2.imread("redhat.jpg")

#only selecting the red part of the image and saving it into another variable
onlyred = cv2.inRange(img,(0,0,200),(40,40,255))

#Displaying original image
cv2.imshow("original",img)

#Displaying only selected red color as a seperate image
cv2.imshow("onlyredd",onlyred)

#holding the frame
cv2.waitKey(0)


