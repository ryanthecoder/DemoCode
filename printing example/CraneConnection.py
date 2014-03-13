# coding: utf-8
import ToolConnection
import sys
import serial
class CraneConnection(ToolConnection):
	def __init__(self, port, buffer = None, file = None):
			self.port = port;
			
			if buffer is not None:
				self.buffer = buffer
			
			self.port = serial.Serial('/dev/ttyUSB0', 115200, timeout=0.5)
			self.open = false
			
			if file is not None:
				self.file = file
			
			self.working = false
			self.waiting = false
			self.listeners = []
			
		def send(command):
			if self.open:
				self.port.write(command)
				
		def load(file):
			if isinstance(file,str):
				self.file = open(file, 'rb')
				self.data = []
				for line in self.file:
					self.data.append(line)
				ind = 0
				packet = [0,0]
				str = ''
				action = ''
				
				while ind < self.data.count():
					str = self.data.pop(0)
					if compare(str,'') != 0:
						if compare(str,'next command')==0:
							packet = [int(s) for s in self.data.pop(0).split() if s.isdigit()]
							
							actionHeight = packet.pop(0)
							actionLength = packet.pop(0)
							action = ''
							
							while ind < actionLength
								action += self.data.pop(0)
							
							self.listeners.append(HeightListener(actionHeigth,action))
						else
							print('invaid input file)
							system.exit(1)
							
				self.open = true;
		
		def close():
			if file is not None:
				self.file.close()
			if self.open:
				self.port.close()
			self.open = false
			