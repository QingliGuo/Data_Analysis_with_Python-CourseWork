#!/usr/bin/env python3

import pandas as pd
import numpy as np
def snow_depth():
    df = pd.read_csv ("src/kumpula-weather-2017.csv")
#    print (df.shape)
    snow_max = np.max (df[df["Year"] == 2017]['Snow depth (cm)'])
    return snow_max

def main():
    print (f'Max snow depth: {snow_depth()}')

if __name__ == "__main__":
    main()
