import pandas as pd
import os

rootDirectory = "/Users/kanghao/Code/MS4089/datasets/thermal data/benchmark"

df = []


for files in os.listdir(rootDirectory):
    if files.endswith(".csv"):
        filePath = os.path.join(rootDirectory, files)
        data = pd.read_csv(filePath, encoding="latin-1", sep=",").iloc[
            0:19110
        ]  # max 19110 rows
        df.append(data)

df = pd.concat(df).reset_index(drop=True)
df.sort_values(by=["Time"], inplace=True)  # sort ascending by time
df = df.drop(columns=df.columns[6:15])  # drop the channels 2-10 (unused)
df.drop(df.tail(2).index, inplace=True)  # drop last 2 rows for the labels in the data

# Clean the data
df["TimeDiff"] = df["Time"].str.replace(":", "")
df["TimeDiff"] = pd.to_numeric(df["TimeDiff"].iloc[0:-1])  # convert to numeric
df["CENTRAL [°C]"] = df["CENTRAL [°C]"].astype(str)
df["TimeDiffTranslated"] = df["TimeDiff"] - df["TimeDiff"].min()

print(df)

## Store data in csv in rootDirectory
df.to_csv(rootDirectory + "/benchmark.csv", index=False)