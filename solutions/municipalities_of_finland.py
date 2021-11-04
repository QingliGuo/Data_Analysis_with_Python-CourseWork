#!/usr/bin/env python3

import pandas as pd

def municipalities_of_finland():
    df = pd.read_csv ('src/municipal.tsv', sep = "\t", index_col = 0)
    return df["Akaa":"Äänekoski"]
    
def main():
    df = municipalities_of_finland()
    print (df)
if __name__ == "__main__":
    main()
