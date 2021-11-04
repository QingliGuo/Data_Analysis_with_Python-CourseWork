#!/usr/bin/env python3

import numpy as np
import functools

def matrix_power(a, n):
    if n > 0:
        return functools.reduce(lambda x,y: x@y, [ a for i in range (n)])
    elif n == 0:
        return np.eye(a.shape[0])
    elif n < 0:
        b = np.linalg.inv(a)
        return functools.reduce(lambda x,y: x@y, [ b for i in range (abs(n))])

def main():

    A = np.array ([[1,2,3],[3,4,5],[6,4,1]])
    print (matrix_power(A,n=-3))

if __name__ == "__main__":
    main()
