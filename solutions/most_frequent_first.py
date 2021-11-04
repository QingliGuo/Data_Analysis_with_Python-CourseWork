#!/usr/bin/env python3

import numpy as np

def most_frequent_first(a, c):
    A = a   ## used a new variable name for a in the code
    col_i = c   ## used a new variable name for c

    the_col = A[:,col_i]    ## the col which we want to count on the item frequency
    col_uq = np.unique(the_col)     ## we get the unique version of all items in the column
    col_freq = np.array ([np.sum(x == A[:,col_i]) for x in col_uq])     ## calculating the frequency of each item
    ordered_index_uq = np.argsort(col_freq,)[::-1]    ## sort the frequncy array based on the reverse order and returning back their positions
    col_uq_ordered = col_uq[ordered_index_uq]   ##  use the position to sort the uniq items
    
    new_array = np.array([])    
    new_array = A[col_uq_ordered[0] == the_col,:]   ## the row(s) which have the most frequent item

    for i in range (1,len(col_uq_ordered)):
        new_array = np.concatenate((new_array, A[col_uq_ordered[i] == the_col,:]),axis = 0)     ## sorting the oder of rows and concatenate them togher
    
    return new_array
    

def main():
    np.random.seed (3)
    B = np.random.randint(0,10,(6,6))
    B = B.T
    print (most_frequent_first(a = B, c = -1))

if __name__ == "__main__":
    main()
