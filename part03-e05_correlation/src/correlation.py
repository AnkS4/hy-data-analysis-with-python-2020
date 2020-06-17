#!/usr/bin/env python3

from scipy.stats import pearsonr
import numpy as np

def load():
    import pandas as pd
    return pd.read_csv("src/iris.csv").drop('species', axis=1).values

def lengths():
    a = load()
    return pearsonr(a[:,0], a[:, 2])[0]

def correlations():
    a = load()
    return np.corrcoef((a[:,0], a[:, 1], a[:,2], a[:, 3]))

def main():
    print(lengths())
    print(correlations())

if __name__ == "__main__":
    main()
