#!/usr/bin/env python3

import sys

def file_count(filename):
    line_c, word_c, char_c = 0, 0, 0

    with open (filename, "r") as f:
        for line in f:
            line_c += 1
            
            words = line.split()
            word_c += len(words)

            char = list(line)
            char_c += len (char)
    
    return (line_c, word_c, char_c)

def print_results (ff):

    lines,words,characters = file_count (filename = ff)
    print (f'{lines}\t{words}\t{characters}\t{ff}')

def main():
    for i in range(1,len(sys.argv)):
        print_results(ff = sys.argv[i].strip())

if __name__ == "__main__":
    main()
