#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
	with open(filename, 'r') as f:
		res = []
		for n,i in enumerate(f):
			if n!=0:
				pattern = r'(\s*\d{1,3})\s+(\d{1,3})\s+(\d{1,3})\s+(.+)' #(\w+|\w+\s+\w+)
				temp = re.match(pattern, i)
				temp = temp.groups()
				temp = f'{temp[0]}\t{temp[1]}\t{temp[2]}\t{temp[3]}'
				res.append(temp)
	return res

def main():
    print(red_green_blue())

if __name__ == "__main__":
    main()
