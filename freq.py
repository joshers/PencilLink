#!/usr/bin/env python3
import pandas as pd
import sys
import inquirer
import re

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


#Function to sort of normalize TNs
def norm(n):
    n = str(n)
    n = re.sub('[^0-9]', '', n)

    if len(n) == 11 and n[0] not in ["+", "0"]:
        n = re.sub('(^1)', '', n)
    elif len(n) == 13 and n[0] not in ["+", "0"]:
        n = re.sub('(^521)', '52', n)

    return n


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
columnName = str(headerSelection['column'])

#Create Pandas DataFrame for processing from CSV file
df = pd.read_csv(
    file_name,
    usecols=[columnName]
)

#Run function and add 'normalized' numbers to new column in df
df['phoneNumber'] = df[columnName].map(norm)

#Set Variable for Print to Screen
n_by_number = df.groupby("phoneNumber")["phoneNumber"].count().sort_values(ascending=False)

#Export to CSV
df.groupby("phoneNumber")["phoneNumber"].count().sort_values(ascending=False).to_csv('frequency_report.csv')

#Print top 25 to screen
print(n_by_number.head(25))