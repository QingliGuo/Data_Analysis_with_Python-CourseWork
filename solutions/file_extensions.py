#!/usr/bin/env python3

import sys
def file_extensions(filename):
    no_ext = []
    with_ext = {}
    
    with open (filename, "r") as f:
        for line in f:
            line = line.strip()
            if "." in line:     ## for those with extension
                ext= line.split (".")[-1]
                if ext in with_ext:
                    with_ext[ext].append (line)
                else:
                    with_ext[ext] = [line]
            else:       ## for those without extension
                no_ext.append(line)

    return (no_ext, with_ext)

def main():
    
    results = file_extensions(filename = sys.argv[1].strip())
    (f_no_extension, f_with_extension) = results

    print (f'{len(f_no_extension)} files with no extension')    ## print filenames without extension

    if len(f_with_extension) > 0:   ## if there are filenames with extension
        sortedkeys = sorted(f_with_extension, key=str.lower)
        for key in sortedkeys:
            print (f'{key} {len(f_with_extension[key])}')

if __name__ == "__main__":
    main()

