# Paul Caulfield, 2019
# My program will query the data to test some hypotheses 

# Solution adapted from 

## Import numpy which is a package for scientific computing with Python http://www.numpy.org/
import numpy

# use genfromtxt to read in the iris.csv from URL
# this creates a 2 dimensional array named "data", the data read into the array is separated using the comma, which is a delineantor which is used in csv files
# solution adapted from https://stackoverflow.com/a/25614793 & https://stackoverflow.com/a/25614784
data = numpy.genfromtxt("https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/d546eaee765268bf2f487608c537c05e22e4b221/iris.csv", delimiter=',')

sepal_length = data[:,0]
# selects the first column of data in the array and name it sepal_length
sepal_width = data[:,1]
# selects the 2nd column of data in the array and name it sepal_width
petal_length = data[:,2]
# selects the 3rd column of data in the array and name it petal_length
petal_width = data[:,3]
# selects the 4th column of data in the array and name it petal_width
species = data[:,4]
# selects the 5th column of data in the array and names it species
test = (petal_length < 2)
print(test)
# set = [sepal_length, sepal_width, petal_length, petal_width, species]
# while petal_length < 2:
#print(set)
# print(set[:,4])

# display results
