#!/usr/bin/env python3

import numpy as np
import pandas as pd

def last_week():
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    df2 = df.copy()
    df2.replace(["New", "Re"], np.nan, inplace=True)
    #df2[["Pos", "LW"]] = df2[["Pos", "LW"]].astype('float')
    df2 = df2.astype({'LW': 'float'})
    #m = ((df2["Peak Pos"]==df2["Pos"]) | (df2["Peak Pos"]!=df2["LW"]))
    #df2.loc[m, "Peak Pos"] = np.nan
    df2["Peak Pos"].where(lambda x: (df2["Peak Pos"] != df2["Pos"]) | (df2["Peak Pos"] == df2["LW"]), np.nan, inplace=True)
    df2["WoC"] = df2["WoC"] - 1
    df2["Pos"] = df2["LW"]
    df2 = df2[df2["Pos"].notna()]
    df2["LW"] = np.nan
    df2["Pos"] = df2["Pos"].astype('int64')
    #print(df2.sort_values("Pos"))
    for i in range(1, 41):
        if i not in df2["Pos"].values:
            df2 = df2.append([{"Pos":i}])
    df2.sort_values("Pos", inplace=True)
    df2.reset_index(drop=True, inplace=True)
    return df2

def main():
    df = last_week()
    print("Shape: {}, {}".format(*df.shape))
    print("dtypes:", df.dtypes)
    print(df)

if __name__ == "__main__":
    main()
