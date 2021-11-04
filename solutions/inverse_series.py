#!/usr/bin/env python3

import pandas as pd

def inverse_series(s):
    re_s = pd.Series (list(s.index),index = s.values) 
    return re_s

def main():
    s = pd.Series ([1,2,3,3], index = list('abcd'))
    print (inverse_series(s))

if __name__ == "__main__":
    main()
