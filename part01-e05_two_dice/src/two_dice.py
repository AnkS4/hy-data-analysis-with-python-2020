#!/usr/bin/env python3

def main():
    for i in range(1,6):
    	for j in range(1,6):
    		if((i+j)==5):
    			#print("(" + str(i) + "," + str(j) + ")")
    			#print(f"{i,j}")
    			print(f"({i},{j})")

if __name__ == "__main__":
    main()
