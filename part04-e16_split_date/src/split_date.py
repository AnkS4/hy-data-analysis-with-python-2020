#!/usr/bin/env python3

import pandas as pd
import numpy as np

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
    return df2
    '''
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    df = df["Päivämäärä"] #.map(str)
    df = df.str.split(expand=True)
    df.dropna(inplace=True)
    df.columns =  ["Weekday", "Day", "Month", "Year", "Hour"]
    df["Day"] = df["Day"].map(int)
    df["Year"] = df["Year"].map(int)
    df["Hour"] = df["Hour"].map(str)
    df["Hour"] = df["Hour"].str.split(":", expand=True)[0]
    df["Hour"] = df["Hour"].map(int)
    #df["Weekday"].where(lambda x: df["Weekday"]=="ma", "Mon", inplace=True)
    m = df["Weekday"]=="ma"
    df.loc[m, "Weekday"] = "Mon"
    m = df["Weekday"]=="ti"
    df.loc[m, "Weekday"] = "Tue"
    m = df["Weekday"]=="ke"
    df.loc[m, "Weekday"] = "Wed"
    m = df["Weekday"]=="to"
    df.loc[m, "Weekday"] = "Tue"
    m = df["Weekday"]=="pe"
    df.loc[m, "Weekday"] = "Fri"
    m = df["Weekday"]=="la"
    df.loc[m, "Weekday"] = "Sat"
    m = df["Weekday"]=="su"
    df.loc[m, "Weekday"] = "Sun"
    
    m = df["Month"]=="tammi"
    df.loc[m, "Month"] = 1
    m = df["Month"]=="helmi"
    df.loc[m, "Month"] = 2
    m = df["Month"]=="maalis"
    df.loc[m, "Month"] = 3
    m = df["Month"]=="huhti"
    df.loc[m, "Month"] = 4
    m = df["Month"]=="touko"
    df.loc[m, "Month"] = 5
    m = df["Month"]=="kesä"
    df.loc[m, "Month"] = 6
    m = df["Month"]=="heinä"
    df.loc[m, "Month"] = 7
    m = df["Month"]=="elo"
    df.loc[m, "Month"] = 8
    m = df["Month"]=="syys"
    df.loc[m, "Month"] = 9
    m = df["Month"]=="loka"
    df.loc[m, "Month"] = 10
    m = df["Month"]=="marras"
    df.loc[m, "Month"] = 11
    m = df["Month"]=="joulu"
    df.loc[m, "Month"] = 12
    df["Month"] = df["Month"].map(int)
    return df
    '''

def main():
    df = split_date()
    print(df)
       
if __name__ == "__main__":
    main()
