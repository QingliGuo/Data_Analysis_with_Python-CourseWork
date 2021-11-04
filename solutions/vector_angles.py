#!/usr/bin/env python3

import numpy as np
import scipy.linalg
import math

def vector_angles(X, Y):
    
    xx = np.sqrt (np.sum (X ** 2, axis = 1))
    yy = np.sqrt (np.sum (Y ** 2, axis = 1))
    xy = np.sum(X * Y, axis = 1)

    cos_alpha = xy/(xx*yy)  ## calculate cosine(alpha)
    
    cos_alpha_clipped = np.clip(cos_alpha, -1.0, 1.0)   ## clip the values' intervals between [-1,1] for np.arccos

    alpha_radian = np.arccos (cos_alpha_clipped)    ## gives radian version of alpha
    alpha_degree = alpha_radian * (180 /math.pi)    ## transfer radian version to degree version
    return alpha_degree
    

def main():
    np.random.seed(1)
    x = np.random.randint(0, 10, (3,4))
    y = np.random.randint(300,900, (3,4))

    print (vector_angles(x,y))

if __name__ == "__main__":
    main()
