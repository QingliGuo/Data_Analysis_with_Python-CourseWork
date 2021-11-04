#!/usr/bin/env python3

import pandas as pd
import numpy as np
import re

def modify_name (x):
    found = re.search (r'(\w+),?\s+(\w+)', x)
    if found.group(2).capitalize() in ["George","Bill", "Dick","Al"]:
        return " ".join([found.group(i).capitalize() for i in [2,1]])
    else:
        return " ".join([found.group(i).capitalize() for i in [1,2]])

def cleaning_data():
    df = pd.read_csv ("src/presidents.tsv", sep = "\t")
    
    for i in range (df.shape[0]):
        df["President"].values[i] = modify_name (df["President"].values[i])
        df["Vice-president"].values[i] = modify_name(df["Vice-president"].values[i])    
            
    df["Start"] = [int(re.findall (r'\d+',x)[0]) for x in df["Start"]]

    df.loc[df.loc[:,"Last"] == "-","Last"] = np.nan
    df["Last"] = df["Last"].astype("float")

    df.loc[df['Seasons'] == "two", 'Seasons'] = 2
    df['Seasons'] = df['Seasons'].astype("int")
    
    return df

def main():
    print (cleaning_data())

if __name__ == "__main__":
    main()
