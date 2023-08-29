import pandas as pd

# Input the file path of the pyrometer and thermocouple data
pyrometerFilePath = "/Users/kanghao/Code/MS4089/datasets/pyrometer data/conventional.csv"
thermocoupleFilePath = "/Users/kanghao/Code/MS4089/datasets/thermocouple data/BM2 21 Jul 23/BM2.csv"

pyrometer = pd.read_csv(pyrometerFilePath)
thermocouple = pd.read_csv(thermocoupleFilePath,low_memory=False)


outputFilePath = "/Users/kanghao/Code/MS4089/datasets/final/BM2.csv"
# Combine both dataframes together
df = pd.concat([thermocouple, pyrometer], axis = 1)
df.to_csv(outputFilePath, index=True, header=True)