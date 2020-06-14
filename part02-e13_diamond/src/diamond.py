#!/usr/bin/env python3

import numpy as np

def diamond(n):
    A = np.eye(n, dtype=int)
    B = np.flip(A, axis=0)
    B = np.delete(B, -1, axis=1)
    C = np.concatenate((B, A), axis=1)
    D = np.flip(C, axis=0)
    D = np.delete(D, 0, axis=0)
    return np.concatenate((C, D), axis=0)

def main():
    print(diamond(1))

if __name__ == "__main__":
    main()
