#!/usr/bin/env python3

import pandas as pd
from sklearn.linear_model import LinearRegression

def mystery_data():
    df = pd.read_csv("src/mystery_data.tsv", sep="\t")
    model = LinearRegression(fit_intercept=False)
    model.fit(df.iloc[:,0:5], df.iloc[:,5])
    return model.coef_

def main():
    coefficients = mystery_data()
    # print the coefficients here
    for i, co in enumerate(coefficients):
        print(f"Coefficient of X{i+1} is {co}")
    
if __name__ == "__main__":
    main()
