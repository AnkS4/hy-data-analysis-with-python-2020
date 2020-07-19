#!/usr/bin/env python3

def detect_ranges(L):
	l = sorted(L)
	l2 = []
	i = 0
	while l:
		if len(l)==1:
			l2.append(l[0])
			l.pop(0)
		elif l[i+1] == l[i] + 1:
			i += 1
			if i == len(l)-1:
				temp = (l[0], l[i]+1)
				l = []
				l2.append(temp)
		else:
			if i==0:
				l2.append(l[0])
				l.pop(0)
			else:
				temp = (l[0], l[i]+1)
				del l[:i+1]
				l2.append(temp)
				i = 0
	return l2

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    #L = [2, 7, 8, 12]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()
