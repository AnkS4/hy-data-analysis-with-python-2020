#!/usr/bin/env python3

import pandas as pd

def suicide_fractions():
    df = pd.read_csv("src/who_suicide_statistics.csv", index_col="country")
    df["mean_fraction"] = df["suicides_no"]/df["population"]
    df2 = df.groupby("country")[["mean_fraction"]].mean()
    return pd.Series(df2["mean_fraction"])
    
def suicide_weather():
    sf = suicide_fractions()
    temp = pd.read_html("src/List_of_countries_by_average_yearly_temperature.html", index_col="Country")[0]
    #header=0
    temp.rename(columns={"Average yearly temperature (1961–1990, degrees Celsius)":"TempAvg"}, inplace=True)
    temp = pd.to_numeric(temp.iloc[:, 0].str.replace("\u2212", "-"))
    #temp["TempAvg"] = temp["TempAvg"].str.replace("\u2212", "-")
    #temp["TempAvg"] = temp["TempAvg"].astype("float")
    com = pd.concat([sf, temp], axis=1, join="inner")
    #com = temp.merge(sf, left_index=True, right_index=True)
    corr = com["mean_fraction"].corr(com["TempAvg"], method="spearman")
    return (len(sf), len(temp), len(com), corr)

def main():
    sff, tempf, comf, corr = suicide_weather()
    print(f"Suicide DataFrame has {sff} rows")
    print(f"Temperature DataFrame has {tempf} rows")
    print(f"Common DataFrame has {comf} rows")
    print(f"Spearman correlation: {corr}")

if __name__ == "__main__":
    main()
