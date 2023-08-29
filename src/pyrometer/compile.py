import pandas as pd
import numpy as np
import os


df = []
rootDirectory = "/Users/kanghao/Code/MS4089/datasets/pyrometer data"
for files in os.listdir(rootDirectory):
    if files.endswith(".txt"):
        filePath = os.path.join(rootDirectory, files)
        data = pd.read_csv(filePath, 
                           sep="\t", 
                           skiprows=2)
        df.append(data)

df = pd.concat(df).reset_index(drop=True)
df.sort_values(by=['Time'], inplace=True)
df.reset_index(drop=True, inplace=True)

# Rename columns and add peak hold intervals
df = df.rename(columns={"°C": "Two color temperature", 
                        "°C.1": "Internal temperature",
                        "°C.2": "One color temperature wide band", 
                        "°C.3": "One color temperature narrow band"})

# Remove -999.90 values as temperature not detected at the point
df = df.drop(df[df['Two color temperature'] == -999.90].index)
df.reset_index(drop=True, inplace=True)

# add time column with 0.1s gap
df["Peak hold time"] = np.linspace(start=0, 
                             stop=0.1*len(df), 
                             num=len(df),
                             endpoint=False)

# Place Peak hold time column in first index
cols = df.columns.tolist()
cols = cols[-1:] + cols[:-1]
data = df[cols]


# Rename file name to store in the folder within datasets
data.to_csv(rootDirectory + "/BM2.csv", index=False)
