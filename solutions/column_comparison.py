#!/usr/bin/env python3

import numpy as np

def column_comparison(a):
    
    return a[a[:,1] > a[:,-2],:]
    
def main():
    np.random.seed(1)
    A = np.random.randint(0,100,(6,5))
    print (column_comparison(A))
if __name__ == "__main__":
    main()
