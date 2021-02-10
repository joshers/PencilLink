#!/usr/bin/env python3
import pandas as pd
import sys

#Pandas Options
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

file_name = sys.argv[1]

dtypes = {
    " remoteNumber": "string",
    "Frequency": "string",
}
df = pd.read_csv(
    file_name,
    dtype=dtypes,
    usecols=[" remoteNumber"]
)

df['phoneNumber'] = df[' remoteNumber'].astype(str).str[-10:]

#Set Variable for Print to Screen
n_by_number = df.groupby("phoneNumber")["phoneNumber"].count().sort_values(ascending=False)

#Print to CSV
df.groupby("phoneNumber")["phoneNumber"].count().sort_values(ascending=False).to_csv('frequency_report.csv')

print(n_by_number.head(25))
