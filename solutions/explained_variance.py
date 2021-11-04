#!/usr/bin/env python3
import numpy as np
import math
from sklearn.decomposition import PCA
import pandas as pd
import matplotlib.pyplot as plt

def explained_variance():
    df = pd.read_csv("./src/data.tsv", sep = "\t")
    X = df.to_numpy()
    pca=PCA()
    pca.fit(X)
    cov_X = np.cov(X.T)
    v = cov_X.diagonal()
    ev = pca.explained_variance_
    return list(v), list(ev)

def main():
    v, ev = explained_variance()
    
    print ("The variances are:", end=' ')
    for i in range(10):
        print (f'{v[i]:.3f}', end = " ")
    print('')
    
    print ("The explained variances after PCA are:", end=' ')
    for i in range(10):
        print (f'{ev[i]:.3f}', end = " ")
    
    plt.plot(np.arange(1,11), np.cumsum(ev))
    plt.ylabel("cumulative sum")
    plt.show()

if __name__ == "__main__":
    main()
