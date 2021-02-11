#!/usr/bin/env python3
import pandas as pd
import sys
import inquirer

#Pandas Options
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

#Require file variable to be passed when invoking script
try:
    file_name = sys.argv[1]
except:
    print("PencilLink freq.py usage:")
    print("freq.py [filename.csv]")
    sys.exit(1)

dtypes = {
    " remoteNumber": "string",
    "Frequency": "string",
}

#Create list from headers in CSV file
headerList = pd.read_csv(file_name, index_col=0, nrows=0).columns.tolist()

#Prompt user to choose header
header = [
  inquirer.List('column',
                message="Which column contains the data you wish to use?",
                choices=headerList,
            ),
]
headerSelection = inquirer.prompt(header)

#Pull header name selection from inquirer
columnNameUse = str(headerSelection['column']).split()
columnName = str(headerSelection['column'])

#Create Pandas DataFrame for processing from CSV file
df = pd.read_csv(
    file_name,
    dtype=dtypes
)

#Create new column in DataFrame for normalized domestic numbers
df['phoneNumber'] = df[columnName].astype(str).str[-10:]

#Set Variable for Print to Screen
n_by_number = df.groupby("phoneNumber")["phoneNumber"].count().sort_values(ascending=False)

#Export to CSV
df.groupby("phoneNumber")["phoneNumber"].count().sort_values(ascending=False).to_csv('frequency_report.csv')

#Print top 25 to screen
print(n_by_number.head(25))