#!/usr/bin/env python3

import pandas as pd
import re

def read_series():
    flag = True
    all = []
    while flag:

        I = input("Input an index and a value for the series seperated by white space:")
        I = I.strip()
        if I == "":
            flag = False
        else:
            all.append(I)
#    all = ["a  12", "b    3", "c 50", ""]
    value_a = []
    index_a = []

    for i in all:
#        print (i)
        if " " in i and len(i.split())==2:
            ind, v = i.split()
            index_a.append(ind)
            value_a.append(str(v))

#            found = re.search(r'(\w+)\s+(\w+)',i)
#            index_a.append(found.group(1))
#            value.append(found.group(2))
#    print (values)
    print (value_a == ["12","3","50"])
    a_s = pd.Series (value_a, index = index_a)
    print (a_s.dtype)
    print (a_s.values.dtype)
    print (a_s.index)
    return a_s

def main():
    print (read_series())
    
if __name__ == "__main__":
    main()
