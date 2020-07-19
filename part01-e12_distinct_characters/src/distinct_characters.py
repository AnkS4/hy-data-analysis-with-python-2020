#!/usr/bin/env python3

def distinct_characters(L):
	d = {}
	for i in L:
		l = len(set(i))
		d[i] = l
	return d

def main():
    print(distinct_characters(["check", "look", "try", "pop"]))

if __name__ == "__main__":
    main()
