import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

x = np.array([1,2,3,4,5,6,7,8]).reshape(-1,1)
y = np.array([12,18,25,35,45,55,65,78])

model = LinearRegression()
model.fit(x,y)
y_pred = model.predict(x)
score = r2_score(y,y_pred)
print("R2_Score of the model is",score)

plt.scatter(x,y)  #actual data 
plt.plot(y,y_pred)   #predicted line

plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.title("Study Hours VS Marks :-")
plt.show()