#!/usr/bin/env python3

import numpy as np
import pandas as pd

def create_series(L1, L2):
    ind = ['a', 'b', 'c'] #list("abc")
    s1 = pd.Series(L1, ind)
    s2 = pd.Series(L2, ind)
    return (s1, s2)
    
def modify_series(s1, s2):
    s1['d'] = s2['b']
    del s2['b']
    return (s1, s2)
    
def main():
    L1 = [1, 3, 7]
    L2 = [2, 5, 0]
    s1, s2 = create_series(L1, L2)
    print(s1, s2)
    s1, s2 = modify_series(s1, s2)
    print(s1, s2)
    print(s1+s2)
    
if __name__ == "__main__":
    main()
