#salary_data.csv file is attached with this file (practice set)

import pandas as pd 
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt 
from sklearn.metrics import r2_score
import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv("salary_data.csv")
print(df.head())

x = df[['Experience']]
y  = df[['Salary']]

model = LinearRegression()
model.fit(x,y)

y_pred = model.predict(x)
score = r2_score(y,y_pred)
print(score)

#prediction :-
prediction = model.predict([[9]])
print("Predicted Salary for 9 years is :", prediction)

#good way:-
from sklearn.model_selection import train_test_split

x_train , x_test , y_train , y_test = train_test_split(x,y,test_size=0.20,random_state=42)

model.fit(x_train , y_train)
y_pred = model.predict(x_test)
score = r2_score(y_test,y_pred)
print("Score:" , score)

# To run the code using good way comment the line from 17-25
# and to run in simple way comment from line 27 to last 