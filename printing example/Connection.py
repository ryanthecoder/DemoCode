# coding: utf-8
## this class provides the abstraction for any type of connection over a port

class Connection:

	def __init__(self, port, buffer = None, file = None):
		self.port = port
		self.buffer = []
		self.open = false
		if file is not None:
			self.file = file
			self.load(file)
	
	##This function should send whatever command is passed to it to the port, but only if the connection has been opened
	@classmethod
	def send(command):
		if self.open:
			print(command)
	
	## This method loads all of the required instance data to establish a connection with the given port from a file
	## It should then open that port.
	@classmethod
	def load(file):
		self.file = file
	
	## closes the port connection and any open files associated with this object
	@classmethod
	def close():
		self.open = false
	
	## Returns a list of boolean values associated with the current state of the object.
	@classmethod
	def getState():
		result = []
		result.append(self.open)
		return result
		