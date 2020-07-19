#!/usr/bin/env python3

import pandas as pd

def main():
    df = pd.read_csv("src/municipal.tsv", sep="\t")
    print(f"Shape: {df.shape[0]},{df.shape[1]}")
    print("Columns:")
    for i in df:
        print(i)

if __name__ == "__main__":
    main()
