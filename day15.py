# Day 16 - Sales Insight Generator

import pandas as pd

# 1️⃣ Load the CSV file
df = pd.read_csv("sales.csv")

# Show first few rows (optional)
print("Data Preview:\n", df.head())


# 2️⃣ Basic Analysis

# Total Sales
total_sales = df["Sales"].sum()
print("\nTotal Sales:", total_sales)

# Average Sales
avg_sales = df["Sales"].mean()
print("Average Sales:", avg_sales)

# Best Selling Product
best_product = df.groupby("Product")["Sales"].sum().idxmax()
print("Best Selling Product:", best_product)


# 3️⃣ Products with sales greater than average
print("\nProducts with Sales > Average:")
above_avg = df[df["Sales"] > avg_sales]
print(above_avg)


# 4️⃣ Add new column "Performance"
# If sales > average → High, else Low
df["Performance"] = df["Sales"].apply(
    lambda x: "High" if x > avg_sales else "Low"
)


# 5️⃣ Sort data by Sales (descending order)
df_sorted = df.sort_values(by="Sales", ascending=False)

print("\nSorted Data with Performance:\n", df_sorted)


# 6️⃣ Save updated data to new CSV (Bonus)
df_sorted.to_csv("updated_sales.csv", index=False)

print("\n✅ Updated file saved as 'updated_sales.csv'")