# coding: utf-8
import Listener
class HeightListener(Listener):
	def _init_(self,height,action,tool):
		self.height = height
		self.action = action
	
	def getEvent():
		return self.height
	
	def getAction():
		return self.action
	
	def getTool():
		return self.tool