# MQ3 SENSOR CODE

""" 
If you have not installed the Wiring Pi Library,
install it using below command : 

sudo pip install wiringpi

"""

#Copy and Paste the below code and save it as a ".py" file

import wiringpi as wiringpi
from time import sleep

wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(25, 0)
count=0
while(count<20):
	my_input=wiringpi.digitalRead(25)
	if(my_input):
		print("Not Detected !")
	else:
		print("Alcohol Detected")
	count=count+1
	sleep(1)