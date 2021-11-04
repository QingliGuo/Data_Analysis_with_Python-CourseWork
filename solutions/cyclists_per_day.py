#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt


def cyclists_per_day():
    df_cyc = pd.read_csv ("src/Helsingin_pyorailijamaarat.csv",sep = ";")
    df1_cyc = df_cyc.dropna(axis = 0, how="all")
    df2_cyc = df1_cyc.dropna(axis = 1, how="all")

    df3_cyc = df2_cyc["Päivämäärä"].copy()
    df4_cyc = df3_cyc.str.split(expand = True)
    df4_cyc.columns = ["Weekday", "Day", "Month", "Year", "Hour"]
    df4_cyc["Hour"] = df4_cyc["Hour"].str.split(":",expand=True).iloc[:,0]

    days = {"ma": "Mon", "ti" : "Tue", "ke" : "Wed", "to" : "Thu", "pe":"Fri", "la":"Sat", "su":"Sun"}
    df4_cyc['Weekday'] = df4_cyc['Weekday'].map(days)

    months = {"tammi":"1","helmi" :"2","maalis": "3","huhti": "4","touko": "5", "kesä": "6",
            "heinä": "7","elo" :"8", "syys" :"9", "loka": "10", "marras": "11", "joulu": "12"}
    df4_cyc["Month"] = df4_cyc["Month"].map(months)

    df4_cyc = df4_cyc.astype({"Weekday" : object, "Day" : int, "Month" : int, "Year" : int, "Hour" : int})

    df = pd.concat([df4_cyc,df2_cyc.drop(columns = ["Päivämäärä"])],axis = 1).drop(columns = ["Weekday", "Hour"])
      
    grouped_df = df.groupby(["Year", "Month", "Day"])

    cyclists_every_day = grouped_df.sum()
    
    return  cyclists_every_day

def main():
    df = cyclists_per_day()
    df1 = df.loc[(2017,8)]  ## how to select rows from multiple index pandas DF

    plt.plot(df1)
    plt.show()

if __name__ == "__main__":
    main()
