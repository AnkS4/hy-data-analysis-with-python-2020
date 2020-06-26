#!/usr/bin/env python3

import pandas as pd

def snow_depth():
    df = pd.read_csv("src/kumpula-weather-2017.csv", index_col=0)
    return max(df.iloc[:, 5]) #df["Snow depth (cm)"].max()

def main():
    val = snow_depth()
    print(f"Max snow depth: {val:.1f}")

if __name__ == "__main__":
    main()
