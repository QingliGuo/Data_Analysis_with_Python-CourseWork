#!/usr/bin/env python3

def interleave(*lists):
    LL = list(zip (*lists))
    
    c_LL = []
    for i in LL:
        c_LL.extend(i)

    return c_LL

def main():
    print(interleave([1, 2, 3,4,4,4,4], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()
