#!/usr/bin/env python3

import sys
import numpy as np

def summary(filename):
    f = open (filename,"r")
    L = f.readlines()
    LL = []
    for x in L:
        try: 
            LL.append (float (x.strip()))
        except ValueError: 
##            sys.stderr.write(f'Not able to transfer "{x.strip()}" to a float number\n') 
            continue

    total = sum(LL)
    ave = sum(LL)/len(LL)
    std = np.sqrt(sum([(x - ave) ** 2 for x in LL])/(len(LL) - 1))
    return (total,ave,std)

def print_results(ff):
    total, average, sd = summary(filename = ff)
    print (f'File: {ff} Sum: {total:.6f} Average: {average:.6f} Stddev: {sd:.6f}')

def main():

    for i in range(1,len(sys.argv)):    ## looping through all input files and make the calculation and print out the results
        print_results (ff = sys.argv[i].strip())

if __name__ == "__main__":
    main()
