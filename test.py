# Paul Caulfield, 2019
# My program will filter data using petal length to identify species with petal length less than 2cm
# I subtracted the standard deviation from the mean to get 2 as the filter value.

# Solution adapted from https://www.geeksforgeeks.org/python-filtering-data-with-pandas-query-method/

# importing pandas package 
import pandas as pd 
  
# making data frame from csv file  
data = pd.read_csv("iris.csv") 

# Filter data where Petal length < 2?
result = data.query('petal_length < 2')

# display
print(result)