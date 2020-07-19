#!/usr/bin/env python3

def merge(L1, L2):
	l2 = []
	l = L1 + L2
	#for i, j in enumerate(l):
	while(l):
		temp = min(l)
		l2.append(temp)
		l.pop(l.index(temp))
	return l2

def main():
	L1 = [1, 7, 8]
	L2 = [4, 10, 11]
	L = merge(L1, L2)
	print(L)

if __name__ == "__main__":
    main()
