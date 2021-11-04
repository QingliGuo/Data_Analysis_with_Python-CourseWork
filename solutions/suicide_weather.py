#!/usr/bin/env python3
import numpy as np
import pandas as pd

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

def suicide_weather():
    html = pd.read_html("src/List_of_countries_by_average_yearly_temperature.html", index_col=0, header = 0)
    df_weather = html[0]
    df_weather.iloc[:,0] = df_weather["Average yearly temperature (1961–1990, degrees Celsius)"].str.replace(u"\u2212", "-").astype(float)
    rnum_df_weather = df_weather.shape[0]

    df_s = pd.read_csv("src/who_suicide_statistics.csv", index_col = 0)
    s = suicide_fractions()
    correlation = s.corr(df_weather["Average yearly temperature (1961–1990, degrees Celsius)"],method='spearman')
    
    rnum_df_s = s.shape[0]
    
    rnum_common = len(list (set (list(df_weather.index.values)) & set (list(s.index.values))))

    return (rnum_df_s, rnum_df_weather, rnum_common, correlation)

def main():
    a,b,c,d = suicide_weather()
    print (f'Suicide DataFrame has {a} rows\nTemperature DataFrame has {b} rows')
    print (f'Common DataFrame has {c} rows\nSpearman correlation: {d:.1f}')

if __name__ == "__main__":
    main()
