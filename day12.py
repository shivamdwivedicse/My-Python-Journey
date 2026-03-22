#sales.csv is attached to this file 

import pandas as pd 
import matplotlib.pyplot as plt 

df = pd.read_csv("sales.csv")
print(df.head())

#Total sales per product(bar)
grouped = df.groupby("Product")["Sales"].sum()
print(grouped)

grouped.plot(kind="bar")
plt.title("Sales VS Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.show()

# #Sales trend
df["Sales"].plot(kind="line")
plt.title("Sales Trends")
plt.xlabel("Index")
plt.ylabel("Sales")
plt.show()

#High sales highlight 

high_sales = df[df["Sales"]>150]
high_sales.groupby("Product")["Sales"].sum().plot(kind="bar", color = "green")

plt.title("Sales greater then 150")
plt.show()

#pie chart 
grouped.plot(kind="pie" , autopct='%1.1f%%')

plt.title("Sales Distribution")
plt.ylabel("")
plt.show()