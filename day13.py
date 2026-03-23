import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")

grouped = df.groupby("Product")["Sales"].sum()

plt.figure(figsize=(10,6))

# 1 Bar chart
plt.subplot(2,2,1)
grouped.plot(kind='bar')
plt.title("Total Sales per Product")

# 2 Line chart
plt.subplot(2,2,2)
df["Sales"].plot(kind='line')
plt.title("Sales Trend")

# 3 Pie chart
plt.subplot(2,2,3)
grouped.plot(kind='pie', autopct='%1.1f%%')
plt.title("Sales Distribution")
plt.ylabel("")

# 4 High sales
plt.subplot(2,2,4)
df[df["Sales"] > 150].groupby("Product")["Sales"].sum().plot(kind='bar')
plt.title("High Sales Products")

plt.tight_layout()
plt.show()