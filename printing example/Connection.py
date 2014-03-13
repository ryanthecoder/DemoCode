# coding: utf-8
class Connection:

	    def __init__(self, port, buffer = None, file = None):
			self.port = port;
			
			self.buffer = []
			
			self.open = false
			
			if file is not None:
				self.file = file
		
		def send(command):
			if self.open:
				print(command)
		
		def load(file):
			self.file = file
		
		def close():
			self.open = false
		
		def getState():
			result = []
			result.append(self.open)
			return result
			