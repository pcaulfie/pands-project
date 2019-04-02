# # Paul Caulfield, 2019
# My program reads in the iris.csv file and calculates some summary statistics.

import numpy

data = numpy.genfromtxt('iris.csv', delimiter=',')

firstcol = data[:,0]
meansepal_length = numpy.mean(data[:,0])

print("Average of sepal_length is: ", meansepal_length)