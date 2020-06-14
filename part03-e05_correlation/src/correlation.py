#!/usr/bin/env python3

import scipy.stats
import numpy as np

def load():
    import pandas as pd
    return pd.read_csv("src/iris.csv").drop('species', axis=1).values

def lengths():
    return 0

def correlations():
    return np.array([])

def main():
    print(lengths())
    print(correlations())

if __name__ == "__main__":
    main()
