import pandas as pd
import os
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

directory = "/Users/kanghao/Code/MS4089/datasets/thermal data/ph300"
df = pd.read_csv(directory + "/preheated.csv", sep=",", low_memory=False)
print(df)

# Interpolate the data
interpolator = interp1d(df["TimeDiffTranslated"], df["CENTRAL [°C]"], kind="linear")
interpolatedTime = pd.RangeIndex(
    start=0, stop=int(df["TimeDiffTranslated"].max()), step=1
)
interpolatedTemp = interpolator(interpolatedTime)

print(interpolatedTime)
# Plot the thermal history
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(interpolatedTime, interpolatedTemp)
ax.autoscale(enable=True, axis="y", tight=True)
plt.xlabel("Time (seconds)")
plt.ylabel("Temperature (°C)")
plt.title("Preheated to 300°C Build Thermal History")
plt.show()
