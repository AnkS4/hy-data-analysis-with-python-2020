#!/usr/bin/env python3

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def fit_line(x, y):
    model=LinearRegression(fit_intercept=True)
    model.fit(x[:,np.newaxis], y)
    return model.coef_[0], model.intercept_
    
def main():
    n=20
    x = np.linspace(0, 10, n)
    y = x*2 + 1 + 1*np.random.randn(n)
    coef, intercept = fit_line(x, y)
    print(f"Slope: {coef}")
    print(f"Intercept: {intercept}")
    plt.plot(x, y, 'o')
    xfit = np.linspace(0,10,100)
    yfit = coef*xfit + intercept
    plt.plot(xfit, yfit, color="black")
    plt.show()
    
if __name__ == "__main__":
    main()
