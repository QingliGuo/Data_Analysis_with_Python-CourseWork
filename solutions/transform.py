#!/usr/bin/env python3

def transform(s1, s2):
    
    L1 = s1.split()
    L2 = s2.split()
    if (len(L1) == len(L2) and len(L1)>0): 
        def trans (x):
            return int(float (x))
        LL1 = list(map(trans, L1))
        LL2 = list(map(trans, L2))
        merged = list(zip (LL1, LL2))

        func = lambda x : x[0] * x[1]
        results = list(map (func, merged))

        return results
    else:
        return []

def main():
    print (transform("1 5 3","2 6 -1"))

if __name__ == "__main__":
    main()
