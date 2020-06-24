#!/usr/bin/env python3

import pandas as pd

def growing_municipalities(df):
    df2 = df[df["Population change from the previous year, %"]>0]
    return df2.shape[0]/df.shape[0]

def main():
    df = pd.read_csv("src/municipal.tsv", sep="\t", index_col=0)
    df = df["Akaa":"Äänekoski"]
    per = growing_municipalities(df)
    print(f"Proportion of growing municipalities: {per:.1f}%")

if __name__ == "__main__":
    main()
