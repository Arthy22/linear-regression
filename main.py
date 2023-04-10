import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

x_dummy=[]
y_dummy=[]

data = pd.read_excel("table.xlsx")
for index, row in data.iterrows():
    x_dummy.append(float(row["x"]))
    y_dummy.append(float(row["y"]))

x = np.array(x_dummy)
y = np.array(y_dummy)
n = np.size(x)

x_m = np.mean(x)
y_m = np.mean(y)

sxy = np.sum((y - y_m) * (x - x_m))
sxx = np.sum((x - x_m) ** 2)

b1 = sxy / sxx
b0 = y_m - b1 * x_m
print("Slope b1 is:", b1)
print("Intercept b0 is:", b0)
print("The equation of line is:y=" + str(b1) + "x+" + str(b0))
y_pre = b1 * x + b0

plt.scatter(x, y, c="blue")
plt.plot(x, y_pre, c="red")
plt.xlabel("Independent variable x")
plt.ylabel("Dependent variable y")
plt.show()

error = y - y_pre
sq_er = np.sum(error ** 2)
mean_sq_er = sq_er / n
root_mean_sq_er = np.sqrt(mean_sq_er)
syy = np.sum((y - y_m) ** 2)
R = 1 - (sq_er / syy)

print("Squared error is:", sq_er)
print("Mean Squared error is:", mean_sq_er)
print("Root mean square error is:", root_mean_sq_er)
print("R squared is:", R)
