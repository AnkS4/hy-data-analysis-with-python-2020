#!/usr/bin/env python3

def transform(s1, s2):
	s1 = map(int, s1.split())
	s2 = map(int, s2.split())
	t = [i*j for i,j in zip(s1, s2)]
	return t

def main():
    print(transform("1 5 3", "2 6 -1"))

if __name__ == "__main__":
    main()
