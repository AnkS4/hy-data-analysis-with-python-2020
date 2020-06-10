#!/usr/bin/env python3

import re

def word_frequencies(filename):
	res = {}
	with open(filename, 'r') as f:
		for i in f:
			temp = re.findall(r'(\S*)', i)
			temp = [i.strip("""!"#$%&'()*,-./:;?@[]_""") for i in temp]
			for i in temp:
				#i!=''
				if i not in res:
					res[i] = 1
				else:
					res[i] += 1
	return res

def main():
    print(word_frequencies('src/alice.txt'))

if __name__ == "__main__":
    main()
