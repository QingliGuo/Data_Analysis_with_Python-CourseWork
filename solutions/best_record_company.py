#!/usr/bin/env python3

import pandas as pd

def best_record_company():
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep = "\t")
    best_company = df.groupby ("Publisher")['WoC'].sum().sort_values(ascending=False).index[0]
    return df[df["Publisher"] == best_company ]

def main():
    print (best_record_company())
    

if __name__ == "__main__":
    main()
