import toPy
from Mirror_Data import Mirror_Data

#Sensor Configuration
#
#	0 -------------	1
#	-----------------
#	------SCREEN-----
#	-----------------	
#	2 -------------	3
#
#-----------------------------------------
#State Codes
#
#-1:No sensor event
#0:Channel 0 sensor event
#1:Channel 1 sensor event
#2:Channel 2 sensor event
#3:Channel 3 sensor event
#4:Channel 0->1 sensor sweep event
#5:Channel 0->2 sensor sweep event
#6:Channel 1->0 sensor sweep event
#7:Channel 1->3 sensor sweep event
#8:Channel 2->0 sensor sweep event
#9:Channel 2->3 sensor sweep event
#10:Channel 3->1 sensor sweep event
#11:Channel 3->2 sensor sweep event
#
#-----------------------------------------

toPy.toPy_start()

event_lst = []
cap_flag = 0

while(1):
	event = toPy.toPy()
	
	#Optional for Debugging
	#print "Sensor Event : " + str(event)
	
	if(event >= 0): #Start capturing
		cap_flag = 1

	if(cap_flag == 1): #Start capturing
		event_lst.append(event) #Append events to list
	
		if(len(event_lst) >= 10): #Check last 10 events for state
			flags = []
			state = -1

			for e in event_lst: #State Machine
				if(state == -1):
					state = e
				if(state == 0):
					if(e == 1):
						state = 4
					if(e == 2):
						state = 5
				if(state == 1):
					if(e == 0):
						state = 6
					if(e == 3):
						state = 7
				if(state == 2):
					if(e == 0):
						state = 8
					if(e == 3):
						state = 9
				if(state == 3):
					if(e == 1):
						state = 10
					if(e == 2):
						state = 11
		
			print "State : " + str(state)
			cap_flag = 0
			event_lst = []
	  
toPy.toPy_end()
