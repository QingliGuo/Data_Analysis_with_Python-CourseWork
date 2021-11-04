#!/usr/bin/env python3

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def fit_line(x, y):

    model = LinearRegression()
    m = model.fit(x[:,np.newaxis], y)
    slope, intercept = m.coef_[0], m.intercept_
    return (slope, intercept)
    
def main():
    data_size = 50
    X = 20 * np.random.rand(data_size)    
    generate_y = lambda x, data_size : x * 23 - 232 + np.random.normal(200, 100, data_size)

    np.random.seed(23)
    Y = generate_y(X,50)

    slope, intercept = fit_line (X, Y)

    print (f'Slope: {slope:.1f}\nIntercept: {intercept}')

    model = lambda x : slope * x + intercept

    X_test = np.linspace(np.min(X),np.max(X),500)
    Y_test = model(X_test[:,np.newaxis])

    plt.plot (X , Y, "o")
    plt.plot(X_test, Y_test)
    plt.show()

if __name__ == "__main__":
    main()
