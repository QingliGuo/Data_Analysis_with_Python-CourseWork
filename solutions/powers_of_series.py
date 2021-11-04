#!/usr/bin/env python3

import pandas as pd
import numpy as np

def powers_of_series(s, k):
    df = pd.DataFrame(np.array([s.values ** (i+1)for i in range(k)]).T, columns = list(range(1,k+1)), index = s.index)
    return df
    
def main():
    s = pd.Series([-1,-2,3,4], index=list("abcd"))
    print (powers_of_series(s,4))
    
if __name__ == "__main__":
    main()
