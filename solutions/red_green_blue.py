#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
    colors = []
    with open (filename, "r") as F:
        for line in F:
            line = line.strip()
            if re.match(r'\A\!', line):
                continue
            else:
                L = re.search (r'\A\s?(\d+)\s+(\d+)\s+(\d+)\s+(\w+.*)\Z', line)
                L_joined = "\t".join (list(L.groups()))
                colors.append (L_joined)

    return colors


def main():
    print(red_green_blue(filename="src/rgb.txt"))

if __name__ == "__main__":
    main()
