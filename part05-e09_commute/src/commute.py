#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt

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

def bicycle_timeseries():
    df = split_date()
    df["Date"] = pd.to_datetime(df[["Year", "Month", "Day", "Hour"]])
    df.drop(columns=["Year", "Month", "Day", "Hour"], inplace=True)
    df.set_index("Date", inplace=True)
    return df

def commute():
    df = bicycle_timeseries()
    df = df["2017-08-01":"2017-08-31"]
    
    days = dict(zip("Mon Tue Wed Thu Fri Sat Sun".split(), range(1,8)))
    df["Weekday"] = df["Weekday"].map(days)
    return df.groupby("Weekday").sum()
    '''
    df = df.groupby(pd.datetime.weekday).sum() #df.groupby(df.index.weekday).sum()
    df["Weekday"] = list(range(1, 8))
    df = df.set_index("Weekday")
    return df
    '''
    
def main():
    df = commute()
    #print(df)
    plt.plot(df)
    weekdays="x mon tue wed thu fri sat sun".title().split()
    plt.gca().set_xticklabels(weekdays)
    plt.show()


if __name__ == "__main__":
    main()
