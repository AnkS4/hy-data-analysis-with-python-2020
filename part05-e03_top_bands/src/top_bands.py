#!/usr/bin/env python3

import pandas as pd

def top_bands():
	df1 = pd.read_csv("src/bands.tsv", sep="\t")
	df1["Band"] = df1["Band"].str.upper()
	df2 = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
	df = pd.merge(df2, df1, left_on='Artist', right_on='Band')
	return df

def main():
	df = top_bands()
	print(df.head())

if __name__ == "__main__":
    main()
