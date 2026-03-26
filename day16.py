import pandas as pd
df = pd.read_csv("sales.csv")
product = input("Enter product (A/B/C): ").upper()

if product in df["Product"].values:

    # Filter data
    filtered = df[df["Product"] == product]
    print("\nFiltered Data:\n", filtered)

    total = filtered["Sales"].sum()
    print("Total Sales:", total)

    avg = filtered["Sales"].mean()
    print("Average Sales:", avg)

else:
    print("❌ Product not found")

# best product
best = df.groupby("Product")["Sales"].sum().idxmax()
print("\nBest Selling Product Overall:", best)