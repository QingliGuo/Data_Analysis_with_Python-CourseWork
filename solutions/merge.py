#!/usr/bin/env python3

def merge(L1, L2):
    LL1 = L1.copy()  ## because it is referred to the original L1; and list is a mutable object, so we need to give the copied value to a new variable to avoid the changes; 
    LL2 = L2.copy()
    total_len = len (LL1+LL2)
#    print ("total", total_len)
    ordered_merged = []
    count = 0   ## count used to break the loop once we have compared all items in both list.
    
    for i in range (total_len): ## For each iteration, we will select the larger item from the fisrt entry of L1 or L2. Then remove the choosed one and compare again.

        if len(LL1) == 0 and len(LL2) > 0 :  ## check if one of the lists have run out of items; if so, we dont have to compare anymore.
            for item in LL2:
                ordered_merged.append(item)
                
            count += len(LL2)

        elif len(LL2) == 0 and len (LL1) > 0:
            for item in LL1:
                ordered_merged.append(item)
            count += len(LL1)

#        print (i, ":", ordered_merged)
        
        if (count == total_len):    ## check if we have take every items from L1 and L2
            break

        x1_min = LL1[0]
        x2_min = LL2[0]

        if x1_min < x2_min:
            ordered_merged.append(x1_min)
            count += 1
            LL1.pop(0)   ## remove the larger item from its list.
        
        elif x1_min > x2_min:
            ordered_merged.append(x2_min)
            count += 1
            LL2.pop(0)

        else:   ## there might be two first items are equal
            ordered_merged.append(x1_min)
            ordered_merged.append(x2_min)
            count += 2
            LL1.pop(0)
            LL2.pop(0)

#        print (ordered_merged)
    
    return ordered_merged

def main():
    L1 = [3,3,6,8,9,32]
    L2 = [1,3,4,6,7]

#    print (L1)
#    print (L2)

    L = merge(L1, L2)
#    print (L)
#    print (L1,"\n",L2)
if __name__ == "__main__":
    main()
