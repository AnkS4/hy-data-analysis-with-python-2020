#!/usr/bin/env python3

import pandas as pd

def best_record_company():
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    #df.groupby("Publisher")[["Publisher","WoC"]].sum() == max(df.groupby("Publisher")[["WoC"]].sum())
    '''
    groups = df.groupby("Publisher")
    num=0
    for i,j in zip(groups,groups["WoC"].sum()):
        if j>num:
            num=j
            df2=i[1]
    return df2
    '''
    return df[df["Publisher"]== df.groupby("Publisher")["WoC"].sum().idxmax()]

def main():
    df = best_record_company()
    print(df)
    
if __name__ == "__main__":
    main()
