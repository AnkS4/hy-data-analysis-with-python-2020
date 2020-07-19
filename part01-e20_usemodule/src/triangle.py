"""This module provides some functions for right-angled triangle."""

__version__ = "1.0"
__author__ = "Aniket Satbhai"

import math

def hypothenuse(a, b):
	"""This function returns the length of the hypothenuse 
	when given the lengths of two other sides of a right-angled triangle."""
	return math.sqrt(a**2 + b**2)

def area(a, b):
	"""This function returns the area of the right-angled triangle,
	when two sides, perpendicular to each other, are given as parameters."""
	return (1/2)*a*b