#!/usr/bin/env python3

def positive_list(L):
    def positive (x):
        return x > 0
    results = list (filter (positive,L))
    return results

def main():
    print (positive_list([2,-2,0,1,-7]))

if __name__ == "__main__":
    main()
