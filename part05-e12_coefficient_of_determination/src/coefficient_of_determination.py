#!/usr/bin/env python3

import pandas as pd
from sklearn import linear_model


def coefficient_of_determination():
    df = pd.read_csv("src/mystery_data.tsv", sep="\t")
    X = df.iloc[:,0:5]
    y = df.iloc[:,5] #df.Y
    reg = linear_model.LinearRegression()
    reg.fit(X, y)
    scores = []
    scores.append(reg.score(X, y))
    for i in X:
        reg.fit(df[i].values.reshape(-1, 1), y)
        score = reg.score(df[i].values.reshape(-1, 1), y)
        scores.append(score)
    return scores
    
def main():
    scores = coefficient_of_determination()
    for i, n in enumerate(scores):
        if i==0:
            print(f"R2-score with feature(s) X: {n}")
        else:
            print(f"R2-score with feature(s) X{i+1}: {n}")
    
if __name__ == "__main__":
    main()
