#!/usr/bin/env python3

import pandas as pd
import numpy as np

def suicide_fractions():
    df = pd.read_csv("src/who_suicide_statistics.csv")
#    df_nona = df.dropna(axis= 0)
#    return df.groupby("country"). apply(lambda df : np.mean (df["suicides_no"].values / df["population"].values))
    
    groups = df.groupby("country")
    
    mean_suicide = []
    s_index = []
    for country, df in groups:
        df_key = df[df ["country"] == country]
        df_key2 = df_key.loc[df_key['suicides_no']>=0,['suicides_no','population']]     ## deal with NAs in ['suicides_no'] in each group
        df_key3 = df_key2.loc[df_key2['population']>=0,['suicides_no','population']]    ## deal with NAs in ['population'] in each group
        s_index.append (country)
        if df_key3.shape[0] > 1 :   ## if there is data left in the dataframe
            mean_suicide.append(np.mean(df_key3['suicides_no'].values/df_key3["population"].values))
        else:       ## if there is no data left in the dataframe
            mean_suicide.append(np.nan)

    s = pd.Series(mean_suicide, index = s_index)
    s.index.name = "country"

    return (s)

def main():
    print (suicide_fractions())

if __name__ == "__main__":
    main()
