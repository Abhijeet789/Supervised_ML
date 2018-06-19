#this is the program to perform some operaations on array


#importing libraries
import numpy 
import os

#taking the input for matrix-1 from user
x=int(input("\nEnter the number of rows of matrix1"))
y=int(input("\nEnter the number of coloumns of matrix1"))
val = int(input("\nEnter the value of element of matrix1"))

#taking the input for matrix-2 from user
x1=int(input("\nEnter the number of rows of matrix2"))
y1=int(input("\nEnter the number of coloumns of matrix2"))
val1 = int(input("\nEnter the value of element of matrix2"))


#creating the array 
array1 = numpy.full((x,y),val)
array2 = numpy.full((x1,y1),val1)

print(array1)
print(array2)

#displaying the menu
X = '''
	press 1 for addition of two matrix
	press 2 for substraction of two matrix
	press 3 for multiply of two matrix
	press 4 for division of two matrix
'''
print (X)

#taking the input from the user to perform perticular operation implemented by if-else
choice = int(input("enter your choice"))

if choice == 1:
	add = numpy.add(array1, array2)
	print(add)
	numpy.savetxt('k11.txt', add,fmt = '%d')


elif choice == 2:
	sub = numpy.subtract(array1, array2)
	print(sub)
	numpy.savetxt('k11.txt', sub)


elif choice == 3:
	mul = numpy.multiply(array1, array2)
	print(mul)
	numpy.savetxt('k11.txt', mul)


elif choice == 4:
	div = numpy.divide(array1, array2)
	print(div)
	numpy.savetxt('k11.txt',div)


else :
	print("\nYou have entered a wrong input")

#taking the input of staoring location from user
loc = input("\nPlease enter the location where you wants to save the outputs ")

#saving the output array on user define location
os.system("touch /home/keshav/"+loc+"/k13.txt | mv k11.txt /home/keshav/"+loc+"/k13.txt")

 
