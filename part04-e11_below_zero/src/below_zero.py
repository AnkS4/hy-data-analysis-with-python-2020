#!/usr/bin/env python3

import pandas as pd

def below_zero():
    df = pd.read_csv("src/kumpula-weather-2017.csv")
    return sum(df["Air temperature (degC)"]<0)

def main():
    sub0 = below_zero()
    print(f"Number of days below zero: {sub0}")
    
if __name__ == "__main__":
    main()
