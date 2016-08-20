

import numpy as np
from pylab import *

# Function returns a list of deviations from the mean
def de_mean(x):
    xmean = mean(x)
    return [xi - xmean for xi in x] #Go through every element in x and called it xi, and return xi-mean for each

def covariance(x,y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n-1)
    
pageSpeeds = np.random.normal(3.0, 1.0, 1000)
purchaseAmount = np.random.normal(50.0, 10.0, 1000)

scatter(pageSpeeds, purchaseAmount)
print covariance(pageSpeeds, purchaseAmount)
# The covariance value recieved is very small, no
# real relationship between pageSpeeds and purchaseAmount
# However we can make a real relationship:
purchaseAmount = np.random.normal(50.0, 10.0, 1000)/ pageSpeeds
scatter(pageSpeeds, purchaseAmount)
print covariance(pageSpeeds, purchaseAmount)
# Now we have a large negative covariance 
# But having a correlation value is more useful since we 
# are able to normalize by the standard deviations, making
# each values relevant in comparable to eachother
def correlation(x,y):
    stddevx = x.std()
    stddevy = y.std()
    return covariance(x,y) / stddevx / stddevy

correlation(pageSpeeds, purchaseAmount)

#Our numpy package can do correlations instantly:
np.corrcoef(pageSpeeds, purchaseAmount)

#Rememember correlation does not imply casaution. 
#For example faster page load speeds does not have to
#cause more puchases (even though they may be related),
#It could have a third casaution factor - faster load 
#speed could simply mean that the user has a faster connection
