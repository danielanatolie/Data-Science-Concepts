import numpy as np
from scipy.stats import norm 
import matplotlib.pyplot as plt
x = np.arange(-3,3,0.001)
plt.plot(x, norm.pdf(x))
plt.plot(x, norm.pdf(x,1.0,0.5)) #values, mean, sd
plt.savefig('/Users/DanLam/Dropbox/ridentcode/DataScience/Practice/MyPlot.png', format='png')
plt.show()

# XKCD - kiddy style:
# plt.xkcd()

#Axes modification
axes = plt.axes()
axes.set_xlim([-5,5]) #Restrict x borders
axes.set_ylim([0, 1.0]) #Restrict y borders
axes.set_xticks([-5,-4,-3,-2,-1,0,1,2,3,4,5]) #Scale of x
axes.set_yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]) #Scale of y


#Grid 
axes.grid()

#Axes label and legend:
plt.xlabel('Productivity')
plt.ylabel('Probability')
plt.legend(['Daniel', 'David'], loc=4) #loc represents location


#Color modification:
plt.plot(x, norm.pdf(x), 'b-') #Blue solid-line
plt.plot(x, norm.pdf(x, 1.0, 0.5), 'r-.') #Red faint line
# -- would mean dashed -. would mean -.-.-. style
#plt.show()


# XKCD removal: 
plt.rcdefaults()

#Pie Chart
values = [1, 5, 7, 20, 30]
colors = ['b', 'm', 'g', 'c', 'm']
explode = [0,0,0.5,0,0]
labels = ['Bangladesh', 'Panama', 'Cuba', 'Russia', 'China']
plt.pie(values, colors= colors, labels=labels, explode= explode)
plt.title('Wealth Locations')

#Bar chart
values = [1,2,3,4]
colors = ['r', 'g', 'b', 'c', 'a']
plt.bar(range(0,5), values, color=colors)
plt.show()

#Scatter plot
from pylab import randn
X = randn(500)
Y = randn(500)
plt.scatter(X,Y)

#Histogram
# plt.hist(data, buckets)

#Box and Whisker Plot
uniformSkewed = np.random.rand(100) * 100 - 40
high_outliers = np.random.rand(10) * 50 + 100
low_outliers = np.random.rand(10) * -50 -100
data = np.concatenate((uniformSkewed, high_outliers, low_outliers))
plt.boxplot(data)
plt.show()
