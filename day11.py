#sales data anlysis project 
#sales.csv is attached with this file

import pandas as pd 
df = pd.read_csv("sales.csv")
print(df.head())

#Basic analysis 
#total sales:-
print("Total sales", df["Sales"].sum())
#avg sales:-
print("Average sales", df["Sales"].mean())
#maximum sale
print("Maximum sales", df["Sales"].max())

#Groupby
grouped = df.groupby("Product")["Sales"].sum()
print(grouped)

#best selling product
print("Best product",grouped.idxmax())

#filter high sales :- 
high_sales = df[df["Sales"]>150]
print(high_sales)

#clean data :- 
df = df.drop_duplicates()
df["Sales"] = df["Sales"].fillna(df["Sales"].mean())

#sort data:-
print(df.sort_values(by="Sales",ascending = False))