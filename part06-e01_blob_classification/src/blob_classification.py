#!/usr/bin/env python3

import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
from sklearn import datasets
from sklearn.model_selection import train_test_split

def blob_classification(X, y):
    return 0.0

def main():
    X,y = datasets.make_blobs(100, 2, centers=2, random_state=2, cluster_std=2.5)
    print("The accuracy score is", blob_classification(X, y))
    a=np.array([[2, 2, 0, 2.5],
                [2, 3, 1, 1.5],
                [2, 2, 6, 3.5],
                [2, 2, 3, 1.2],
                [2, 4, 4, 2.7]])
    accs=[]
    for row in a:
        X,y = datasets.make_blobs(100, int(row[0]), centers=int(row[1]),
                                  random_state=int(row[2]), cluster_std=row[3])
        accs.append(blob_classification(X, y))
    print(repr(np.hstack([a, np.array(accs)[:,np.newaxis]])))

if __name__ == "__main__":
    main()
