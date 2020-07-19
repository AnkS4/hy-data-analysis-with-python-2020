#!/usr/bin/env python3

import pandas as pd

def read_series():
    ind = []
    val = []
    while True:
        txt = input("Enter: ")
        if not txt:
            break
        try:
            i, v = txt.split()
            ind.append(i)
            val.append(v)
        except ValueError:
            print("ValueError")
            continue
    return pd.Series(val, index=ind, dtype='object')

def main():
    print(read_series())

if __name__ == "__main__":
    main()
