#!/usr/bin/env python3

def find_matching(L, pattern):
	index = []
	for n, i in enumerate(L):
		if pattern in i:
			index.append(n)
	return index

def main():
    index = find_matching(["sensitive", "engine", "rubbish", "comment"], "en")
    print(index)

if __name__ == "__main__":
    main()
