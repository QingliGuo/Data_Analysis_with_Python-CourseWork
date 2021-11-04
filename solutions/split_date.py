#!/usr/bin/env python3

import pandas as pd
import numpy as np

def split_date():
    df = pd.read_csv ("src/Helsingin_pyorailijamaarat.csv", sep = ";")
    df1 = df.dropna(axis = 0, how="all")
    df2 = df1.dropna(axis = 1, how="all")
    df3 = df2["Päivämäärä"].copy()
    df4 = df3.str.split(expand = True)
    df4.columns = ["Weekday", "Day", "Month", "Year", "Hour"]
    df4.loc[:,'Hour'] = df4.loc[:,'Hour'].str.split(":", expand = True).iloc[:,0].astype("int32")
    df4.loc[:, ['Day','Year']] = df4.loc[:, ['Day','Year']].astype("int32")    
    
    week = {"ma": "Mon", "ti" : "Tue", "ke" : "Wed", "to" : "Thu", "pe":"Fri", "la":"Sat", "su":"Sun"}

    for key, value in week.items():
        df4.loc[df4["Weekday"] == key,"Weekday"] = value

    month = {"tammi":"1","helmi" :"2","maalis": "3","huhti": "4","touko": "5", "kesä": "6",
            "heinä": "7","elo" :"8", "syys" :"9", "loka": "10", "marras": "11", "joulu": "12"}
    for key, value in month.items():
        df4.loc[df4["Month"] == key, "Month"] = value
    df4.loc[:, 'Month'] = df4.loc[:, 'Month'].astype("int32")    
    return df4

def main():
    print (split_date().head())
       
if __name__ == "__main__":
    main()
