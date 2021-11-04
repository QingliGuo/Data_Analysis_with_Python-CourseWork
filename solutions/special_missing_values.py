#!/usr/bin/env python3

import pandas as pd
import numpy as np

def special_missing_values():
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv",sep = "\t")
    df.loc[df['LW'] == "Re",:] = None
    df.loc[df['LW'] == "New",:] = None
    df1 = df.dropna(axis = 0)
    df1.loc[:,'LW'] = list(df1['LW'].astype('int32'))

    return df1.loc[df1['LW'] < df1['Pos'],:]   ## The improving means the position will be getting smaller and smaller. 

def main():
    print (special_missing_values())

if __name__ == "__main__":
    main()
