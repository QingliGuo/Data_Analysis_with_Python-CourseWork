#!/usr/bin/env python3

def detect_ranges(L):

    L_sorted = []
    LL = L.copy()

    ## Sort L
    for ii in range (len(L)-1):
        min_tmp =   LL[0]
        for i in range(1,len(LL)):
            if min_tmp > LL[i]:
                min_tmp = LL[i]

        LL.remove(min_tmp)
        L_sorted.append(min_tmp)

        if len(LL) == 1:
            L_sorted.append(LL[0])
            break

    ## geting the range of sorted L
    L_range = []

    flag = True     ## marking if the search for new interval should be open or not
    
    print (L_sorted)
    i = 0
    while i < len(L_sorted)-1:
        
        if flag:
            start = L_sorted[i]
            end = L_sorted[i]

        for j in range(i+1, len(L_sorted)):
            
            x1 = L_sorted[j-1]  ## the upstream value in the current interval.
            x2 = L_sorted[j]    ## the current value in the interval

            if x2 == x1 + 1 :   ## check if x2 is the expected value to extend the interval
                flag = False    ## the interval continues because the current observed value is the expected one
                end = x2 + 1    ## extend the end of the interval
                
            else:
                flag = True     ## the current interval terminated
                
                if start == end:    ## check if the interval is a single value or not
                    L_range.append(start)
                else:
                    L_range.append((start,end))

                if j == len(L_sorted) - 1:  ## if we only left one item which is not included in the current interval, we assign it as single value;
                    L_range.append(L_sorted[j])
                break                
        i = j   ## move the start search position from i to index j

        if i == len(L_sorted) - 1 and flag == False:    ## for the case that the interval includes the last item
            if start == end:
                L_range.append(start)
            else:
                L_range.append((start,end))

    return L_range

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()

