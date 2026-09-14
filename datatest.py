import pandas as pd
import matplotlib.pyplot as plt

data = {
    "weight": [4.17, 5.58, 5.18, 6.11, 4.50, 4.61,
               5.17, 4.53, 5.33, 5.14, 4.81, 4.17,
               4.41, 3.59, 5.87, 3.83, 6.03, 4.89,
               4.32, 4.69, 6.31, 5.12, 5.54, 5.50,
               5.37, 5.29, 4.92, 6.15, 5.80, 5.26],
    "group": ["ctrl"] * 10 + ["trt1"] * 10 + ["trt2"] * 10
}

PlantGrowth = pd.DataFrame(data)

above_55 = PlantGrowth[PlantGrowth["weight"] > 5.5]

group_counts = above_55["group"].value_counts()

group_counts.plot(
    kind="bar",
    color=["yellow", "purple", "white"], #vikings colors!
    edgecolor="black"
)

plt.xlabel("Group")
plt.ylabel("Number of Plants")
plt.title("Plants With Weight Above 5.5")

plt.show()