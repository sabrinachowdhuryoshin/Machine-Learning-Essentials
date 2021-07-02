#linear regression on google stocks

import pandas as pd

#read the csv data
df = pd.read_csv("GOOG.csv")  

#chosen important features
df = df[['adjOpen','adjClose','adjVolume','adjHigh','adjLow']]

#finding the percentage of imortant features
df['HL_PCT'] = (df['adjHigh'] - df['adjLow']) / df['adjClose'] *100

#finding the daily percent change
df['PCT_change'] = (df['adjClose'] - df['adjOpen']) / df['adjOpen'] *100

#choosing the important parameters to print
df = df [['adjClose', 'HL_PCT', 'PCT_change', 'adjVolume']]
print(df.head())