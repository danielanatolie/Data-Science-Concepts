# Linear Regression - fitting a straight line to a set up observations 

# Gradient descent is an alternative to linear regression

# Coefficient of determination (R-squared), how well does the 
# line fit for the data (1 being a perfect fit)
import numpy as np 
from pylab import *

pageSpeeds = np.random.normal(3.0, 1.0, 1000)
purchaseAmount = 100 - (pageSpeeds + np.random.normal(0.,0.1,1000))*3

plt.scatter(pageSpeeds, purchaseAmount)
plt.show()

from scipy import stats
slope, intercept, r_value, p_value, std_err = stats.linregress(pageSpeeds, purchaseAmount)
print r_value ** 2 #Linear relationship between web speed and purchace

#Plotting a regression line:
import matplotlib.pyplot as plt
def predict(x):
    return slope * x * intercept
    
fitLine = predict(pageSpeeds)
plt.scatter(pageSpeeds, purchaseAmount)
plt.plot(pageSpeeds, fitLine, c='r')
plt.show()

