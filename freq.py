#!/usr/bin/env python3
import pandas as pd

dtypes = {
    "numbers": "string",
    "short_number": "string",
}
df = pd.read_csv(
    "numbers.csv",
    dtype=dtypes,
    usecols=["numbers"]
)

# print(df)
df['short_number'] = df['numbers'].astype(str).str[-10:]

n_by_number = df.groupby("short_number")["short_number"].count().sort_values(ascending=False)

print(n_by_number)