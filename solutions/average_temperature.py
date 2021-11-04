#!/usr/bin/env python3
import numpy as np
import pandas as pd

def average_temperature():
    df = pd.read_csv ("src/kumpula-weather-2017.csv")
    return np.mean (df[df["m"] == 7]["Air temperature (degC)"])

def main():
    print (f'Average temperature in July: {average_temperature()}')

if __name__ == "__main__":
    main()
