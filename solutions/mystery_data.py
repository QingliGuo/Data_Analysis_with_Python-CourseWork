#!/usr/bin/env python3

import pandas as pd
from sklearn.linear_model import LinearRegression

def mystery_data():
    df = pd.read_csv ("src/mystery_data.tsv", sep = "\t")
    X = df.iloc [:,:-1].values
    Y = df.iloc [:, -1].values
    model = LinearRegression(fit_intercept= False)
    m = model.fit (X,Y)
    
    return m.coef_

def main():
    coefficients = mystery_data()
    for i in range(len(coefficients)):
        name = "X" + str(i+1)
        print (f"Coefficient of {name} is {coefficients[i]}")

    # print the coefficients here
    
if __name__ == "__main__":
    main()
