# coding: utf-8
import Connection
class ToolConnection(Connection):
	def __init__(self, port, file = None):
		self.port = port;
		self.serial = port
		self.buffer = []
			
		self.port = port
		
		self.open = false
		
		if file is not None:
			self.file = file
		
		self.working = false
		self.waiting = false
		self.listeners = []
	
		def send(command):
			if self.open:
				print(command)
		
		def load(file):
			if isinstance(file,str):
				self.file = open(file, 'rb')
			self.open = true;
		
		def close():
			if file is not None:
				self.file.close()
			self.open = false
		
		def getListeners():
			return self.listeners
			
		def getState():
			result = []
			result.append(self.open)
			result.append(self.working)
			result.append(self.waiting)
		
