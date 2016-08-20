# Multivariate Regression (multiple regression)
# Used where more than one variables effects the other
# ex. price of the car: brand, style, speed, are example 
# of variable effect the price of the car
# The final model would look something like:
# price = const + const2*var1 + const3*var2 + const4*var3
# Where the constants are the coefficients, you can simply 
# remove variables that have a low value (close to 0) coefficient.

import pandas as pd #Used to manipulate data sheets (ex. splitting)
import statsmodels.api as sm
df = pd.read_excel('http://cdn.sundog-soft.com/Udemy/DataScience/cars.xls')
df.head() #Head provides the first few samples of the data-set


df['Model_ord'] = pd.Categorical(df.Model).codes #Categorical-codes converts text into numbers 
X = df[['Mileage', 'Model_ord', 'Doors']]
y = df[['Price']]

X1 = sm.add_constant(X)
est = sm.OLS(y, X1).fit() 

print est.summary()

#If you are not dealing with Normalized data it is more import to look at standard errors
# judging by the standard errors, milleage is the most important factor since it has the lowest standard error

y.groupby(df.Doors).mean()
