import pandas as pd
data = {
  "Name": ["Amit", "Deepak", "Ravi", "Neha"],
  "Marks": [78, None, 90, 82]
}
df = pd.DataFrame(data)
print(df)

# Check Missing Values*

print(df.isnull())
# Count missing values:
print(df.isnull().sum())

# Remove Missing Values*

df = df.dropna()
print(df)

# This removes rows with missing data.

# Fill Missing Values*

# Instead of removing rows:

df["Marks"] = df["Marks"].fillna(0)
# Or fill with mean:
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

#Remove Duplicate Rows*

# Example:
df = pd.DataFrame({
  "Name": ["Amit","Deepak","Deepak","Ravi"],
  "Marks": [78,85,85,90]
})
print(df.duplicated())

# Remove duplicates:
df = df.drop_duplicates()

#Rename Columns*

df.rename(columns={"Marks":"Score"}, inplace=True)

#Change Data Types*

df["Marks"] = df["Marks"].astype(int)
