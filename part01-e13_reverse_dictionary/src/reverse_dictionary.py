#!/usr/bin/env python3

def reverse_dictionary(d):
	d2 = {}
	val = []
	for _, i in d.items():
		for i2 in i:
			val.append(i2)
	val = list(set(val))
	for v in val:
		temp = []
		for i, j in d.items():
			if v in j:
				temp.append(i)
		d2[v] = temp
	return d2

def main():
    d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    print(reverse_dictionary(d))

if __name__ == "__main__":
    main()
