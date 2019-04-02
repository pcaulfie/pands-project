# # Paul Caulfield, 2019
# My program reads in the iris.csv file and calculates some summary statistics.

import numpy
import matplotlib.pyplot as plt

data = numpy.genfromtxt('iris.csv', delimiter=',')
# solution adapted from https://stackoverflow.com/a/25614793
sepal_length = data[:,0]
sepal_width = data[:,1]
petal_length = data[:,2]
petal_width = data[:,3]
meansepal_length = numpy.nanmean(data[:,0])
meansepal_width = numpy.nanmean(data[:,1])
meanpetal_length = numpy.nanmean(data[:,2])
meanpetal_width = numpy.nanmean(data[:,3])
# numpy.nanmean used to calculate the mean, ignoring NaNs.) source https://stackoverflow.com/q/51720631
# NaN means "Not a Number"; a flag to which indicates that the "operation's operands lie outside its domain" https://people.eecs.berkeley.edu/~wkahan/ieee754status/IEEE754.PDF

print("Average of sepal_length is: ", meansepal_length)
print("Average of sepal_width is: ", meansepal_width)
print("Average of petal_length is: ", meanpetal_length)
print("Average of petal_width is: ", meanpetal_width)

plt.hist(sepal_length)

plt.show()