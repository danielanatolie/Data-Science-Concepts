#Generating 10,000 incomes ranging from $15000 to $27000
import numpy as np
incomes=np.random.normal(27000, 15000, 10000)
#(center, sd, amountOfData)
print np.mean(incomes)

#Ploting a histogram of the data
import matplotlib.pyplot as plt
#plt.hist(incomes, 50)
#plt.show()

#Median of income data
print np.median(incomes)

#How outlier effects data set
incomes = np.append(incomes, [1000000000])
np.median(incomes)
#Mean is most affected
print np.mean(incomes)

#Mode Analysis
ages = np.random.randint(18, high=90, size=500)
# print ages
from scipy import stats
print stats.mode(ages)
