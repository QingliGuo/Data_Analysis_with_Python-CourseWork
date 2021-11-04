#!/usr/bin/env python3
import numpy as np
import pandas as pd

def below_zero():
    df = pd.read_csv ("src/kumpula-weather-2017.csv")
    return np.sum (df['Air temperature (degC)'] < 0)

def main():
    print (f'Number of days below zero: {below_zero()}')
    
if __name__ == "__main__":
    main()
