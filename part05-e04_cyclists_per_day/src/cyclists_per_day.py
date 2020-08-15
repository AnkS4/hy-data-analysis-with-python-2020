#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt


def cyclists_per_day():
	df = split_date()
	df2 = df.copy()
	df2.drop(["Weekday", "Hour"], axis=1, inplace=True)
	return df2.groupby(["Year", "Month", "Day"]).sum()
    
def split_date():
	df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
	df2 = df["Päivämäärä"].str.split(expand=True)
	df2.dropna(inplace=True)
	df2.columns =  ["Weekday", "Day", "Month", "Year", "Hour"]
	df2["Hour"] = df2["Hour"].str.split(":", expand=True)[0]
	
	days = dict(zip("ma ti ke to pe la su".split(), "Mon Tue Wed Thu Fri Sat Sun".split()))
	months = dict(zip("tammi helmi maalis huhti touko kesä heinä elo syys loka marras joulu".split(), range(1,13)))
	
	df2["Weekday"] = df2["Weekday"].map(days)
	df2["Month"] = df2["Month"].map(months)
	df2 = df2.astype({"Weekday": object, "Day": int, "Month": int, "Year": int, "Hour": int})
	
	df.drop("Päivämäärä", axis=1, inplace=True)
	df.dropna(axis=0, how='all', inplace=True)
	df.dropna(axis=1, how='all', inplace=True)
	#df.dropna(axis=0, how="all", inplace=True).dropna(axis=1, how="all", inplace=True)
	df = pd.concat([df2, df], axis=1)
	return df

def main():
    df = cyclists_per_day()
    print(df)
    #df2 = df.sum(axis=1)
    #print(df2)
    
    #df = df.reset_index()
    #df3 = df.loc[(df["Month"]==8) & (df["Year"]==2017)]
    #print(df3)
    #df4 = df3.sum(axis=1)
    #plt.plot(df4)
    
    df = df.loc[(2017, 8), :]
    print(df)
    df.plot()
    plt.show()
    
if __name__ == "__main__":
    main()
