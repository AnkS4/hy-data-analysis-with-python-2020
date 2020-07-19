#!/usr/bin/env python3

import sys
import re

def file_count(filename):
	lines = 0
	words = 0
	chars = 0
	with open(filename, 'r') as f:
		for i in f:
			lines += 1
			w = re.findall(r'(\S+)', i)
			words += len(w) #len(i.split())
			chars += len(i) #sum(len(i) for i in w)
	return (lines, words, chars)

def main():
    for i in sys.argv[1:]:
    	l, w, c = file_count(i)
    	print(f"{l}\t{w}\t{c}\t{i}")

if __name__ == "__main__":
    main()
