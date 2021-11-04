#!/usr/bin/env python3

def find_matching(L, pattern):
    index_list = []
    for i,x in enumerate(L):
        if pattern in x:
            index_list.append(i)
    return index_list

def main():
    print (find_matching(["sensitive", "engine", "rubbish", "comment"], "en"))

if __name__ == "__main__":
    main()
