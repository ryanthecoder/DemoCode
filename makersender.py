# coding: utf-8
import makerbot_driver, serial
import sys
import struct
import threading
import time
import math
print str('starting')

#Instantiate Makerbot Driver and prepare it for file and tty communications
r = makerbot_driver.s3g()
makerbotSerial = serial.Serial('/dev/ttyACM0',115200,timeout=1)
condition = threading.Condition()
r.writer = makerbot_driver.Writer.StreamWriter(makerbotSerial,condition)
input = makerbot_driver.FileReader.FileReader()

#TODO add file selection
input.file =open('Stretchlet.x3g','rb')

#load x3g code into memory 
#readFile automatically figures out what command is next and useing the formating of x3g retrives the data for that command
#each payload can be varying sizes
payloads = input.ReadFile(callback=True)
for p in payloads:
	#store instruction
	cmd = p[0]
	
	#find data format for payload
	fmt = str('<B'+''.join(makerbot_driver.FileReader.hostFormats[cmd]))
	
	#tool action commands have extra payloads of varying length
	if cmd == makerbot_driver.host_action_command_dict['TOOL_ACTION_COMMAND'] :
		fmt = str(fmt+''.join(makerbot_driver.FileReader.hostFormats[p[1]]))
		
	#pack the payload into a packet for sending to the the makerbot
	payload = struct.pack(fmt, *p)
	
	#current hack onto the percent complete command to tell when to pause the printer. (here it happens at 4 percent)
	if cmd == 150 and p[1] == 4:
		#TODO stop the extruder head
		
		#drop the bed all the way to the bottom and wait for this action to finish
		r.find_axes_maximums(['z'],100,20)
		while r.is_finished()==False:
			time.sleep(0.1)
		r.extended_stop(True,False)
		
		####################here starts where the other machine is active#############
		print str('waiting on tinyg')
		#create serial connection to other machine here is my machine useing the tinyG
		tinyGserial = serial.Serial('/dev/ttyUSB0', 115200, timeout=0.5)
		
		#load the data that will be sent to this machine
		gcodeFile = open('out.txt','r')
		block = ''
		
		for line in gcodeFile:
			#add commands till the buffer is full
				#NOTE:	buffer size is somewhat arbitrary since the tinyG uses software control to stop buffer overflows, however if this nuber is left out
				#		a bug occures where the tinyG crashes. Im not sure why this happens but I beleive that it is because the resonse buffer overflows
				#		so periodically we need to listen to the tinyG in order to clear out that buffer. 
				#		picking a number that is too small works, however this greatly slows down the machine because it is wasting time waiting for responses
				# 		it is much faster to send a large chunk of data into the buffer and read the output as those instructions are being performed
				
			if sys.getsizeof(block) + sys.getsizeof(line) <= 1024:
				block = block + line
			else:
				#send the next block to the buffer.
				tinyGserial.write(block)
				#wait for response from the tinyG to know that all of the instructions are completeted.
				tinyGserial.readlines(None)
				#restart a new block with the first command that didn't make it into the buffer
				block = line
		#send the last block of instructions to the tinyG
		tinyGserial.write(block)
		tinyGserial.readlines(None)
		######################other machine is done################################
		print str('resuming print')
	else :
		r.writer.send_command(payload)
	#wait for the Makerbot to finish instruction before sending the next one.
	while r.is_finished() ==False:
		time.sleep(0.1)
	
