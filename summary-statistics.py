# # Paul Caulfield, 2019
# My program reads in the iris.csv file and calculates some summary statistics.

import numpy
# Import numpy which is a package for scientific computing with Python http://www.numpy.org/
import matplotlib.pyplot as plt
# Import plyplot module pyplot to generate interactive plots :https://matplotlib.org/users/pyplot_tutorial.html


data = numpy.genfromtxt('iris.csv', delimiter=',')
# use genfromtxt to read in the iris.csv text tile, which is saved in the pands-project directory
# this creates a 2 dimensional array named "data", the data read into the array is separated using the comma, which is a delineantor which is used in csv files
# solution adapted from https://stackoverflow.com/a/25614793 & https://stackoverflow.com/a/25614784

sepal_length = data[:,0]
# selects the first column of data in the array and name it sepal_length
sepal_width = data[:,1]
# selects the 2nd column of data in the array and name it sepal_width
petal_length = data[:,2]
# selects the 3rd column of data in the array and name it petal_length
petal_width = data[:,3]
# selects the 4th column of data in the array and name it petal_width

# Calculate the Mean of each variable
meansepal_length = numpy.nanmean(data[:,0])
# calculate the mean of the first column of data in the array and name it meansepal_length
meansepal_width = numpy.nanmean(data[:,1])
# calculate the mean of the 2nd column of data in the array and name it meansepal_width
meanpetal_length = numpy.nanmean(data[:,2])
# calculate the mean of the 3rd column of data in the array and name it meanpetal_length
meanpetal_width = numpy.nanmean(data[:,3])
# calculate the mean of the 4th column of data in the array and name it meanpetal_width
# numpy.nanmean used to calculate the mean, ignoring NaNs. source https://stackoverflow.com/q/51720631
# NaN means "Not a Number"; a flag to which indicates that the "operation's operands lie outside its domain" https://people.eecs.berkeley.edu/~wkahan/ieee754status/IEEE754.PDF
# Additional reference https://docs.scipy.org/doc/numpy-1.15.1/reference/generated/numpy.nanmean.html
print("Average of sepal_length is: ", meansepal_length)
print("Average of sepal_width is: ", meansepal_width)
print("Average of petal_length is: ", meanpetal_length)
print("Average of petal_width is: ", meanpetal_width)

plt.hist(sepal_length)

plt.show()