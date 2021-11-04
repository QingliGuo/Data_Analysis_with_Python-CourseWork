#!/usr/bin/env python3

import pandas as pd

def cyclists():
    df = pd.read_csv ("src/Helsingin_pyorailijamaarat.csv", sep = ";")
    df1 = df.dropna(axis = 0, how="all")
    df2 = df1.dropna(axis = 1, how="all")
    return df2


def main():
    cyclists()
    
if __name__ == "__main__":
    main()
