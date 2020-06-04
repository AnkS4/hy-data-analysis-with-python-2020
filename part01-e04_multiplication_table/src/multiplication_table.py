#!/usr/bin/env python3


def main():
    for i in range(1,11):
    	for j in range(1, 11):
    		#print(f"{i*1} {i*2} {i*3} {i*4} {i*5} {i*6} {i*7} {i*8} {i*9} {i*10}")
    		print(f"{i*j:3d}", end=" ")
    	print()

if __name__ == "__main__":
    main()
