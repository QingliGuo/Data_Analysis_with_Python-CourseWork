#!/usr/bin/env python3

import pandas as pd


def split_date(df):
    d = df["Päivämäärä"].str.split(expand=True)
    d.columns = ["Weekday", "Day", "Month", "Year", "Hour"]

    hourmin = d["Hour"].str.split(":", expand=True)
    d["Hour"] = hourmin.iloc[:, 0]
    
    days = {"ma": "Mon", "ti" : "Tue", "ke" : "Wed", "to" : "Thu", "pe":"Fri", "la":"Sat", "su":"Sun"} 
    d["Weekday"] = d["Weekday"].map(days)
    
    months = {"tammi":"1","helmi" :"2","maalis": "3","huhti": "4","touko": "5", "kesä": "6",
            "heinä": "7","elo" :"8", "syys" :"9", "loka": "10", "marras": "11", "joulu": "12"}
    d["Month"] = d["Month"].map(months)
    
    d = d.astype({"Weekday": object, "Day": int, "Month": int, "Year": int, "Hour": int})
    return d

def split_date_continues():
    df = pd.read_csv ("src/Helsingin_pyorailijamaarat.csv", sep = ";")
    df1 = df.dropna(axis = 0, how="all")
    df2 = df1.dropna(axis = 1, how="all")
    first = split_date(df2)
    second = df2.drop (columns = ["Päivämäärä"])
    dff = pd.concat([first, second], axis = 1)

    return dff

def main():
    df = split_date_continues()
    print("Shape:", df.shape)
    print("Column names:\n", df.columns)
    print(df.head())


if __name__ == "__main__":
    main()
