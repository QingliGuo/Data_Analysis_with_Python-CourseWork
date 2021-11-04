#!/usr/bin/env python3

def sum_equation(L):
    
    if len(L) > 1:
        L_str = [str(x) for x in L]
        answer = " + ".join(L_str)
        answer += " = " + str(sum(L))
        return answer
    
    elif len(L) == 1:
        answer = str(L) + " = " + str(L)
        return answer

    elif L == []:
        return "0 = 0"

def main():
    print (sum_equation([1,5,7]))

if __name__ == "__main__":
    main()
