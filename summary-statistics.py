# # Paul Caulfield, 2019
# My program reads in the iris.csv file and calculates some summary statistics.

import numpy
import matplotlib.pyplot as plt

data = numpy.genfromtxt('iris.csv', delimiter=',')

sepal_length = data[:,0]
meansepal_length = numpy.nanmean(data[:,0])
# numpy.nanmean used to calculate the mean, ignoring NaNs.) source https://stackoverflow.com/q/51720631
# NaN means "Not a Number"; a flag to which indicates that the "operation's operands lie outside its domain" https://people.eecs.berkeley.edu/~wkahan/ieee754status/IEEE754.PDF

print("Average of sepal_length is: ", meansepal_length)

plt.hist(sepal_length)

plt.show()