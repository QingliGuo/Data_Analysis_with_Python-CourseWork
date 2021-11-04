#!/usr/bin/env python3

import re


def file_listing(filename="src/listing.txt"):
    info = []
    with open (filename, "r") as F:
        for string in F:
#            strings = string.split()
            string = string.strip() ## remove the beginning and ending spaces for the string
            mo = re.search(r'hyad-all\s+(\d+)\s+(\w+)\s+(\d+)\s+(\d{2}):(\d{2})\s+(\S+)\Z',string)
            values = mo.groups() ## return the tuples from the regular pattern matches
            new_values = (int (values[0]), values[1] , int(values[2]), int(values[3]), int(values[4]), values[5]) ## partially change the data type
            info.append(new_values)
    return info

def main():
    information = file_listing(filename="src/listing.txt")
    print (information)
if __name__ == "__main__":
    main()
