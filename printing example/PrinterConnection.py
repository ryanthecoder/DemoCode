# coding: utf-8
import Connection

## This class provieds the abstraction for any kind of printer that is connected
## It extends Connection by added controls for start, pause, resume and also for adding and retriveing listeners
## other tools should add listeners to a PrinterConnection, and PrinterConnection is then responsible for checking to see if those events need to be triggered
class PrinterConnection(Connection):

	def __init__(self, port,file = None):
		self.port = port
		self.serial = port
		self.buffer =[]
		
		self.open = false;
		
	if file is not None:
		self.file = file
		self.load(file)
	## added state definitions, used to make sure the printer is in a certain state before executing commands
	self.isPrinting = false
	self.isPaused = false
	self.isStarted = false
	
	## create a list of listeners that this object has access too				
	self.listeners = []
	
	def send(command):
		if self.open:
			print(command)
	
	## open the file associated with this connection, This file should contain the compiled data for the printer (i.e. GCode or s3G etc)
	def load(file):
		if isinstance(file,str):
			self.file = open(file, 'rb')
		self.open = true;
	
	##close the file and the port	
	def close():
		if file is not None:
			self.file.close()
		self.open = false
	
	##start sending the file that was loaded when load was called
	def start():
		self.isStarted = true
		self.isPrinting = true
	
	## pause the print operations, disable the extruder and clear the print bed so there is room for other tools to work.
	def pause():
		if self.isPrinting:
			self.isPrinting = flase;
			self.isPaused = true;
	
	## return printer position to the point where it was when pause was called and resume sending data to printer
	def resume():
		if self.isPaused:
			self.isPaused = false;
			self.isPrinting = true;
	
	#adds a listener to this object if the printing hasn't started yet
	def addListener(listener):
		assert self.isStarted == true
		self.listeners.append(listener)
	
	## returns the list of listeners associated with this object
	def getListeners():
		return self.listeners
		
	## returns the state of the printer
	def getState():
		result = []
		result.append(self.open)
		result.append(self.isPrinting)
		result.append(self.isPaused)
		result.append(self.isStarted)
		return result;