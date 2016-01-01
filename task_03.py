# usr/bin/env python
# -*- coding: utf-8 -*- 
"""Third task"""


import produce


class Apple(produce.Produce):
	"""Explaning the apple class change
	
	Args:
		None.
	
	Returns: 
		None.
	
	Example: 
		>>> print Apple.duration
		5356800
		>>> print produce.Produce.duration 
		604800
	"""
	duration = 5356800 