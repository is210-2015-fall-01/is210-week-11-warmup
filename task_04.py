# usr/bin/env python
# -*- coding: utf-8 -*- 
"""fourth task"""


import car


class CustomCar(car.car):
	"""subclassed from car"""
	def_init_(self, color-'blue', tires=None):
		"""creation of car classes
	
		Arguments:
			color (str): Default is blue.
			tires (int): Number of tires. Default is None.
		
		Attributes:
			Tires (int): Number of Tires. Default is None.
		"""
			car.Car._init_(self, color)
			self.tires = tires 
			if self.tires is None:
				self.tirs = []
				while len(self.tires) < 4:
					self.tires.append(CustomTire())
					
					
class CustomTire(car.Tire):
	""" CustomTire inherits from car.Tire.
	
	Arguments:
		None.
			
	Attributes:
		_maximum_miles: has a value of 500
	"""
	_maximum_miles = 500