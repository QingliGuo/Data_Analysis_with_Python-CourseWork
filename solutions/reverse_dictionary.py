#!/usr/bin/env python3

def reverse_dictionary(d):
    rev_dict = {}
    for key,value in d.items():
        Finn_num = len(value)
        for single_Finn in value:
            if single_Finn in rev_dict:
                rev_dict[single_Finn].append(key)
            else:
                rev_dict[single_Finn] = [key]

    return rev_dict

def main():
    d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    print (reverse_dictionary(d))

if __name__ == "__main__":
    main()
