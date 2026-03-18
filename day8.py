# PROBLEM :- PREDICT STUDENT MARKS

hours = [1,2,3,4,5,6,7,8]
marks = [10,20,30,40,50,60,70,80]

import numpy as np 
from sklearn.linear_model import LinearRegression
x = np.array([1,2,3,4,5,6,7,8]).reshape(-1,1)
y = np.array([10,20,30,40,50,60,70,80])
print(x)
print(y)

model = LinearRegression()
model.fit(x,y)
prediction = model.predict([[9]])
print("Predicted Marks:", prediction)

