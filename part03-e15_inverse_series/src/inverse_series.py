#!/usr/bin/env python3

import pandas as pd

def inverse_series(s):
    s2 = pd.Series(s.index, s.values)
    return s2

def main():
    s = pd.Series([1, 2, 5, 2, 9], list("abcde"))
    s2 = inverse_series(s)
    print(s2)
    print(s2[2])

if __name__ == "__main__":
    main()
