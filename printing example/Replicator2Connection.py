# coding: utf-8
import makerbot_driver
import serial
import sys
import struct
import threading
import time
import math
import PrinterConnection
import HeightListener

class Replicator2Connection(PrinterConnection):
	def __init__(self, port, file = None):
		self.port = port
		self.serial = serial.Serial(self.port,115200,timeout=1)
		self.buffer = makerbot_driver.s3g()
		self.buffer.writer =  makerbot_driver.Writer.StreamWriter(makerbotSerial,threading.Condition())
			
		self.open = false;
			
		if file is not None:
			self.file = file
			self.load(file)
			
		self.isPrinting = false
		self.isPaused = false
		self.isStarted = false
						
		self.listeners = []
		
	def send(command):
		assert self.open == true
		self.buffer.writer.send_command(command)
	
	def load(file):
		assert type(file) is str
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
			
			
			
			## check to make sure it doesn't trigger a listener
			if cmd == 155:
				for l in self.listeners :
					if (l.getEvent() >= p[3]/400): #400 step/mm taken from Replicator2 profile on Makerbot driver https://github.com/makerbot/s3g/blob/master/makerbot_driver/profiles/Replicator2.json
						self.pause()
						if self.paused == true:
							l.tool.send(l.getAction())
							while l.tool.getState[1]:
								time.sleep(0.1)
							listeners.remove(l)
						self.resume()
			
			self.buffer.writer.send_command(payload)
			while self.buffer.writer.is_finished() ==False:
				time.sleep(0.1)
	
	def pause():
		if self.isPrinting:
			self.isPrinting = flase;
			self.resumePoint = self.buffer.get_extended_position()[0]
			self.buffer.find_axes_maximums(['z'],100,20)
			while self.buffer.is_finished()==False:
				time.sleep(0.1)
			self.buffer.tool_action_command(0,10,0x00)##disable the extruder
			self.isPaused = true;
	
	def resume():
		if self.isPaused:
			self.isPaused = false;
			position = self.buffer.get_extended_position()[0]
			zChange = (position[2]-self.resumePoint[2])/400.0
			self.buffer.queue_extended_point_x3g(self.resumePoint,100,0x00,zChange,0.25)
			self.isPrinting = true;
			
	def addListener(listener):
		assert type(listener) is HeightListener
		self.listeners.append(listener)
	
	def getState() :
		result = []
		result.append(self.open)
		result.append(self.isPrinting)
		result.append(self.isPaused)
		result.append(self.isStarted)
		return result;