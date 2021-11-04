#!/usr/bin/env python3

import pandas as pd

def cycling_weather():
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

    l_df = pd.concat([df4_cyc,df2_cyc.drop(columns = ["Päivämäärä"])],axis = 1)
    
    df_weather = pd.read_csv ("src/kumpula-weather-2017.csv")
    
    merged_df = pd.merge(l_df, df_weather, left_on = ["Year","Month","Day"], right_on = ["Year","m","d"])
    
    merged_df_final = merged_df.drop(columns=["m","d","Time","Time zone"])
    
    return merged_df_final

def main():
    
    print (cycling_weather().head())
    
if __name__ == "__main__":
    main()
