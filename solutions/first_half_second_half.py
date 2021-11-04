#!/usr/bin/env python3

import numpy as np

def first_half_second_half(a):
    ncol = a.shape[1]
    
    sum_of_fisrthalf = np.sum (a[:,:int(ncol/2)],axis = 1)
    sum_of_secondhalf = np.sum (a[:,int(ncol/2):],axis = 1)
    
    return a[sum_of_fisrthalf > sum_of_secondhalf,:]

def main():
    np.random.seed(2)
    A = np.random.randint(0,100,(6,6))
    print (first_half_second_half(A))

if __name__ == "__main__":
    main()
