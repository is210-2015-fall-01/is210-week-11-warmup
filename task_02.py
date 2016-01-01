# usr/bin/env python
# -*- coding: utf-8 -*- 
"""second task"""


import time 


class Snapshot(object): 
	"""This is the Snapshot class.
	
	Arguments:
		None.
	
	Returns:
		created (int): Unix Epoch Time.
		
	Example:
		>>> mysnap = Snapshot() 
		>>> hasattr(mysnap, 'created') 
		True 
	""" 
	def __init__(self):
		self.created = time.time() 