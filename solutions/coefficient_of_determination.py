#!/usr/bin/env python3

import pandas as pd
from sklearn import linear_model
import numpy as np

def coefficient_of_determination():
    df = pd.read_csv ("src/mystery_data.tsv", sep = "\t")
    
    rscore = []
    X = df.iloc [:,:-1].values
    Y = df.iloc [:, -1].values

    model = linear_model.LinearRegression(fit_intercept= True)
    m = model.fit (X,Y)
    rscore.append(m.score(X,Y))

    for i in range(5):
        x = df.iloc [:,i].values
        model = linear_model.LinearRegression(fit_intercept= True)
        m = model.fit (x[:,np.newaxis],Y)
        rscore.append(m.score(x[:,np.newaxis], Y))

    return rscore
    
def main():
    rs = coefficient_of_determination()
    print (f'R2-score with feature(s) X: {rs[0]}')
    for i in range(1,6):
        print (f'R2-score with feature(s) {"X"+str(i)}: {rs[i]}')
if __name__ == "__main__":
    main()
