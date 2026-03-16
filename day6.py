# Find Average of Each Row (NumPy)
import numpy as np 
matrix =np.array([[10,20,30],
                  [40,50,60],
                  [70,80,90]])

row_average = matrix.mean(axis =1)  #axis operate row wise
print(row_average)

# Maximum Value in Each Column
matrix = np.array([[5,8,2],
                   [7,1,9],
                   [4,6,3]])

column_maximum = matrix.max(axis = 0)
print(column_maximum)

# Normalize Data

data = np.array([10,20,30,40,50])
normalized = (data - data.min())/(data.max() - data.min())
print(normalized)

# Find Outliers

data = np.array([10,12,13,14,15,100])
mean = np.mean(data)
std = np.std(data)

outliers = []
for num in data:
    if num > mean+2*std:
        outliers.append(num)
print("Outliers" , outliers)

# Pandas Mini Analysis

import pandas as pd 

data ={
    "Name" : ["A","B","C","D"],
    "Marks": [85,90,78,92]
}
df = pd.DataFrame(data)
print(df)

print("Average mean:" , df["Marks"].mean())
top_student = df.loc[df["Marks"].idxmax()]
print("Top Student:")
print(top_student)