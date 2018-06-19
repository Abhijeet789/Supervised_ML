#this program is to implement use of matrix using numpy

#importing python libraries
import numpy
import os

#taking the inputs from the user
x=int(input("\nEnter the number of rows of matrix"))

y=int(input("\nEnter the number of coloumns of matrix"))

val = int(input("\nEnter the value of element "))

loc = input("\nPlease enter the location where you wants to save the matrix ")

array1 = numpy.full((x,y),val)

numpy.savetxt('k11.txt', array1)

#printing the matrix
print(array1)

os.system("touch /home/keshav/"+loc+"/k12.txt | mv k11.txt /home/keshav/"+loc+"/k12.txt")

 
