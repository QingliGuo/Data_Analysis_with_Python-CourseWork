#!/usr/bin/env python3

import pandas as pd

def swedish_and_foreigners():
    df = pd.read_csv ('src/municipal.tsv', sep = "\t", index_col = 0)
    df1 = df["Akaa":"Äänekoski"]

    df2 = df1[df1["Share of Swedish-speakers of the population, %"] > 5]
    df3 = df2[df2["Share of foreign citizens of the population, %"] > 5]

    df4 = df3[["Population","Share of Swedish-speakers of the population, %","Share of foreign citizens of the population, %"]]
#    print (df3.shape)
    return df4

def main():
    print (swedish_and_foreigners())

if __name__ == "__main__":
    main()
