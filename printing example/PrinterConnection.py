# coding: utf-8
import Connection
class PrinterConnection(Connection):

	    def __init__(self, port,file = None):
			self.port = port
			self.serial = port
			self.buffer =[]
			
			self.open = false;
			
			if file is not None:
				self.file = file
			
			self.isPrinting = false
			self.isPaused = false
			self.isStarted = false
						
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
		
		def start():
			self.isStarted = true
			self.isPrinting = true
		
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
		
		def getListeners():
			return self.listeners
		def getState()
			result = []
			result.append(self.open)
			result.append(self.isPrinting)
			result.append(self.isPaused)
			result.append(self.isStarted)
			return result;