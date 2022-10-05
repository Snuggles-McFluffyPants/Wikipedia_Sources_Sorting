import pandas as pd

from frequent_string_functions import *

# from Text_Input_Window import *
# items = string.split("\n")

import json

# Opening JSON file
f = open('testcase.json', )

# returns JSON object
raw_data = json.load(f)

# Create a Panda DataFrame from list
df = pd.DataFrame(raw_data)

# Rename first column name
# iterating the columns
old_name = 5
for col in df.columns:
    old_name = col

df.rename(columns={old_name: "Full_Raw_Data"}, inplace=True)

# Adding one column to Author with Date Retrieved, and another one with all
# data except for the Author
author_split = df["Full_Raw_Data"].str.split("\"", n = 1, expand = True)
df["Author"]= author_split[0]
df["Minus_Author"] = author_split[1]

# Adding one column to Dataframe with Date Retrieved, and another one with all
# data except for date retrieved
dateRetrieved_split = df["Minus_Author"].str.split("Retrieved", n = 1, expand = True)
df["Date_Retrieved"] = dateRetrieved_split[1]

for i in dateRetrieved_split[0]:
    i = i.replace("Retrieved", "")
df["Minus_Date_Retrieved"] = dateRetrieved_split[0]

# Adding one column to Dataframe with Date Retrieved, and another one with all
# data except for date retrieved
title_split = df["Minus_Date_Retrieved"].str.split("\"", n = 1, expand = True)
df["Title"] = title_split[0]

for i in title_split[1]:
    i = i[2:]
df["Minus_Title"] = title_split[1]

selection = 1
print(df["Title"][selection])
print(df["Minus_Title"][selection])


# print(df["Date_Retrieved"])

# Print the names of all the columns in this dataframe
print("\n")
for col in df.columns:
    print(col)

# df["Index1"] = df["Full_Raw_Data"].str.index("\"")
# var = df["Author"] = df["Full_Raw_Data"].str.split("\"", n=1, expand=False)
# df["Writers"] = var[0]
#
# print(df["Author"])
