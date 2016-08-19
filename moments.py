# Moments - the measure of the shape of the distribution
# First moment: mean
# Second: variance
# Third: Skew - how lop sided data is
# Fourth: kurtosis - how thick is the tail and how sharp is the pick,
#   higher peaks have higher kurtosis
import numpy as np
import matplotlib.pyplot as plt

vals = np.random.normal(0, 0.5, 10000)
plt.hist(vals, 50)
plt.show() 

# First moment:
print "First moment, mean: %f" % np.mean(vals)

# Second moment:
print "Second moment, varaince: %f" % np.var(vals)

# Third moment:
import scipy.stats as sp
print "Third moment, skew: %f" % sp.skew(vals)

# Forth moment:
print "Forth moment, kurtosis: %f" % sp.kurtosis(vals)

