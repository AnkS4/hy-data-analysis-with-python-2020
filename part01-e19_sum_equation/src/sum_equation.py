#!/usr/bin/env python3

def sum_equation(L):
	if not L:
		s = "0 = 0"
	else:
		s = " + ".join(str(i) for i in L)
		s += f" = {str(sum(L))}"
		'''
		s = list(map(str, L))
		s = " + ".join(s) + f" = {sum(L)}"
		'''
	return s

def main():
    print(sum_equation([1,5,7]))

if __name__ == "__main__":
    main()
