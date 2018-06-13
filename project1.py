import time as t
import os
import webbrowser 

menu = '''
	press 1 to see todays date and time
	press 2 to create a file
	press 3 to create a directory
	press 4 to search something on google
	press 5 to restart your system
	press 6 to shut down your system
	press 7 to logout from user    '''
print(menu)
	

choice = int(input( "Please Enter your choice from 1 to 7 "))

if choice == 1 :
	print "You have choosen an option to see todays date and time "
	print "showing todays date and time "
	print t.ctime()


elif choice == 2 :
	print "You have choosen an option to create a file"
	name = raw_input(" Please enter a name of the file you wants to create \n")
	with open(name , "w") as name : 
	 name.write()
	print "file has been created successfully \n "   
													

elif choice == 3 :
	print "You have choosen an option to create a directory"
	name = raw_input("Please enter the name of the directory ")	
	os.makedirs(name)
	print "Directory has been created successfully"	

elif choice == 4:
	print "You have choosen an option to search something on google"
	ans = raw_input("Please enter the text to be searched for ")                                   
	webbrowser.open_new_tab("https://www.google.com/search?source=hp&ei=7QIdW4HhPM_0rQGS5LrgDw&q= " + ans)		


elif choice == 5 :
	print "You have choosen the option to restart your system "
	os.system(" sudo shutdown -r -t 0 ")


elif choice == 6 :
	print "You have choosen an option to shutdown from your system "
	os.system(" sudo shutdown -h -t 1 ") 								


elif choice == 7 :
	print "You have choosen an option to logout from your system "
	os.system(" pkill -KILL -u abhijeet")


else :
	print "You have entered wrong choice "

