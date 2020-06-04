#!/usr/bin/env python3

import math


def main():

	while 1:
		op = input("Choose a shape (triangle, rectangle, circle): ")
		if op == "":
			break
		elif op == "triangle":
			b = int(input("Give base of the triangle: "))
			h = int(input("Give height of the triangle: "))
			a = 0.5 * b * h
			print("The area is ", a)
		elif op == "rectangle":
			w = int(input("Give width of the rectangle: "))
			h = int(input("Give height of the rectangle: "))
			a = w * h
			print("The area is ", a)
		elif op == "circle":
			r = int(input("Give radius of the circle: "))
			a = math.pi * r**2
			print("The area is ", a)
		else:
			print("Unknown shape!")
if __name__ == "__main__":
    main()
