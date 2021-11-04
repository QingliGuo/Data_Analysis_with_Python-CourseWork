#!/usr/bin/env python3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def bicycle_timeseries():
    df_cyc = pd.read_csv ("src/Helsingin_pyorailijamaarat.csv",sep = ";")
    df1_cyc = df_cyc.dropna(axis = 0, how="all")
    df2_cyc = df1_cyc.dropna(axis = 1, how="all")
#    df2_cyc = df2_cyc.drop(columns = ["Päivämäärä"])
#    print (df2_cyc.head())

    df3_cyc = df2_cyc["Päivämäärä"].copy()
    df4_cyc = df3_cyc.str.split(expand = True)
    df4_cyc.columns = ["Weekday", "Day", "Month", "Year", "Hour"]
    df4_cyc["Hour"] = df4_cyc["Hour"].str.split(":",expand=True).iloc[:,0]

    days = {"ma": 1, "ti" : 2, "ke" : 3, "to" : 4, "pe": 5, "la" : 6, "su" : 7}
    df4_cyc['Weekday'] = df4_cyc['Weekday'].map(days)

    months = {"tammi":"1","helmi" :"2","maalis": "3","huhti": "4","touko": "5", "kesä": "6",
            "heinä": "7","elo" :"8", "syys" :"9", "loka": "10", "marras": "11", "joulu": "12"}
    df4_cyc["Month"] = df4_cyc["Month"].map(months)

    df4_cyc = df4_cyc.astype({"Weekday" : object, "Day" : int, "Month" : int, "Year" : int})
#    print (df4_cyc.head())

    df2_cyc['Date'] = pd.to_datetime(df4_cyc[["Year","Month","Day","Hour"]])
    df2_cyc = df2_cyc.set_index ("Date")
    df2_cyc = df2_cyc.drop(columns = ["Päivämäärä"])

    return df2_cyc

def commute():
    df = bicycle_timeseries()
    df1 = df["2017-08-1":"2017-08-31"]
    by_weekday = df1.groupby(df1.index.dayofweek).sum()
    by_weekday.index = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    return by_weekday
    
def main():
    df = commute()
    
    df.plot()
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    
    plt.show()

if __name__ == "__main__":
    main()
