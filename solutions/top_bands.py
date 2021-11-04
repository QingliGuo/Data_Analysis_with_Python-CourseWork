#!/usr/bin/env python3

import pandas as pd

def top_bands():
    df_topband = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep ="\t")
    df_band = pd.read_csv("src/bands.tsv", sep ="\t")
    df_band['Band'] = df_band["Band"].str.upper()
    merged_df = pd.merge(df_topband, df_band,left_on = "Artist", right_on = "Band" )
#    merged_df_final = merged_df.drop(columns = ["Band"])

    return merged_df

def main():
    print (top_bands())

if __name__ == "__main__":
    main()
