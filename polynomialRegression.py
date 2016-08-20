# Polynomial Regression - using a polynomial curve to represent data
from pylab import *
import numpy as np

np.random.seed(2) #results stay the same with this line
pageSpeeds = np.random.normal(3.0, 1.0, 1000)
purchaseAmount = np.random.normal(50.0, 10.0, 1000) / pageSpeeds

plt.scatter(pageSpeeds, purchaseAmount) 
plt.show()

#Polyfit function:
x = np.array(pageSpeeds)
y = np.array(purchaseAmount)

p4 = np.poly1d(np.polyfit(x, y, 4)) #4 is the order of the polynomial

import matplotlib.pyplot as plt
xp = np.linspace(0,7,100)
plt.scatter(x,y)
plt.plot(xp, p4(xp), c='r')
plt.show()

#R^2 error
from sklearn.metrics import r2_score

r2=r2_score(y, p4(x))
print r2 #Our model is a decent fit for the data created