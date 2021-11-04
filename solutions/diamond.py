#!/usr/bin/env python3

import numpy as np

def diamond(n):
    if n == 0:
        return f"{n} cannot be used for making diamond"
    else:
        part2 = np.eye(n,dtype = int)
 
        part2_1 = part2[:-1,:]  ## The right top coner
        part2_2 = part2[-1,:]   ## second half of the middle line

        part1 = part2[:-1,1:]
        part1 = part1[:,::-1]   ## The left top corner

        part3 = np.eye(n,dtype = int)
        part3_1 = part3[0,]     ## The first half of the middle line
        part3_2 = part3[1:,]    ## The left bottom corner 

        part4 = part3[1:,:-1]   
        part4 = part4[:,::-1]   ## The right bottom corner

        top = np.concatenate((part1,part2_1), axis=1)   ## combine the top pannel
        mid = np.concatenate((part3_1.reshape(1,n),part2_2[1:].reshape(1,n-1)),axis = 1)    ## make the middle one line
        bottom = np.concatenate((part3_2,part4), axis=1)    ## cobine the bottom pannel
        dia = np.concatenate((top,mid,bottom))      ##combine three parts together
    
        return dia


def main():
    for i in range (10):
        print (f"{i}-th diamond")
        print (diamond(i))
    
if __name__ == "__main__":
    main()
