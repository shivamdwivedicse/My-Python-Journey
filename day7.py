# Feature Scaling (Standardization)
import numpy as np

data = [10,20,30,40,50]
mean = np.mean(data)
std = np.std(data)
standarized = (data-mean)/std

print(standarized)
print(mean)
print(std)

# Handle Missing Values
dta = np.array([10,20,None , 40, 50],dtype = float)
mean = np.nanmean(dta)
dta[np.isnan(dta)] = mean
print(dta)

# Encode Categorical Data
data = ["Red", "Blue", "Green", "Blue", "Red"]

unique = list(set(data))
encoding = {}
for i , val in enumerate(unique):
    encoding[val] = i
encoded = [encoding[x] for x in data]
print(encoding)
print(encoded)

# Train-Test Split
data = [1,2,3,4,5,6,7,8,9,10]
split = int(0.8*len(data))
print(split)
train =data[:split]
print(train)
test = data[split:]
print(test)

# Mini Data Cleaning Pipeline

import pandas as pd

data = {
    "Age" : [20,25,None,30,35],
    "Salary":[20000,30000,25000,None,40000]
}

df = pd.DataFrame(data)
print(df)

#fill missing values 
df['Age'].fillna(df["Age"].mean() , inplace = True)
df['Salary'].fillna(df["Salary"].mean() , inplace = True)
print(df)

#Normalize 

df['Age'] = (df["Age"] - df["Age"].min())/(df["Age"].max()-df["Age"].min())
df['Salary'] = (df["Salary"] - df["Salary"].min())/(df["Salary"].max()-df["Salary"].min())
print(df)