#!/usr/bin/env python3

import sys
import re
import math

def summary(filename):
	with open(filename, 'r') as file:
		t = file.read()
		mo = re.findall(r'([+|-]*\d+.?\d*)',t)
		a = [float(i) for i in mo]
		l = len(a)
		total = sum(a)
		avg = total/l
		temp = [(i-avg)**2 for i in a]
		std = math.sqrt(sum(temp)/(l-1))
	return (total, avg, std)

def main():
	for i in sys.argv[1:]:
		total, avg, std = summary(i)
		print(f"File: {i} Sum: {total:.6f} Average: {avg:.6f} Stddev: {std:.6f}")

if __name__ == "__main__":
    main()
