import makerbot_driver
import serial
import sys
import struct
import threading
import time
import math
import PrinterConnection
class Replicator2Connection(PrinterConnection):
	def __init__(self, port, buffer = None, file = None):
	
			self.port = serial.Serial('/dev/ttyACM0',115200,timeout=1)
			self.buffer =  makerbot_driver.Writer.StreamWriter(makerbotSerial,threading.Condition())
			
			self.open = false;
			
			if file is not None:
				self.file = file
				self.load(file)
			
			self.isPrinting = false
			self.isPaused = false
			self.isStarted = false
						
			self.listeners = []
		
		def send(command):
			if self.open:
				print(command)
		
		def load(file):
			if isinstance(file,str):
				input = makerbot_driver.FileReader.FileReader()
				input.file = open(file,'rb')
				self.payloads = input.ReadFile(callback=True)
				
		def close():
			if file is not None:
				self.file.close()
			self.open = false
		
		def start():
			self.isStarted = true
			self.isPrinting = true
			for p in self.payloads:
				#store instruction
				cmd = p[0]
				
				#find data format for payload
				fmt = str('<B'+''.join(makerbot_driver.FileReader.hostFormats[cmd]))
				
				#tool action commands have extra payloads of varying length
				if cmd == makerbot_driver.host_action_command_dict['TOOL_ACTION_COMMAND'] :
					fmt = str(fmt+''.join(makerbot_driver.FileReader.hostFormats[p[1]]))
					
				#pack the payload into a packet for sending to the the makerbot
				payload = struct.pack(fmt, *p)
				self.buffer.send_command(payload)
				while r.is_finished() ==False:
					time.sleep(0.1)
		
		def pause():
			if self.isPrinting:
				self.isPrinting = flase;
				self.isPaused = true;
		
		def resume():
			if self.isPaused:
				self.isPaused = false;
				self.isPrinting = true;
				
		def addListener(listener):
			self.listeners.append(listener)
		
		def getState()
			result = []
			result.append(self.open)
			result.append(self.isPrinting)
			result.append(self.isPaused)
			result.append(self.isStarted)
			return result;