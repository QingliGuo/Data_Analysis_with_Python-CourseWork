#!/usr/bin/env python3
import pandas as pd

def create_series(L1, L2):
    s1 = pd.Series(L1,index = list("abc"))
    s2 = pd.Series(L2,index = list("abc"))
    return (s1, s2)
    
def modify_series(s1, s2):
    s1['d'] = s2['b'].copy()
    ss2 = s2.drop(labels=['b'])
    return (s1, ss2)
    
def main():
    LL1 = [1,2,3]
    LL2 = [4,5,6]

    s1, s2 = create_series (LL1,LL2)
    print (s1)
    print (s2)

    ss1 , ss2 = modify_series (s1,s2)
    print (ss1)
    print (ss2)
    
    print (ss1.__add__(ss2))    

if __name__ == "__main__":
    main()
