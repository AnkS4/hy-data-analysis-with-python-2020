#!/usr/bin/env python3

import numpy as np

def first_half_second_half(a):
    l = a.shape[1]//2
    return a[np.sum(a[:,:l], axis=1)>np.sum(a[:,l:], axis=1)]

def main():
    a = np.array([[1, 3, 4, 2],
                  [2, 2, 1, 2]])
    print(first_half_second_half(a))

if __name__ == "__main__":
    main()
