# Paul Caulfield, 2019
# My program will test some hypotheses 

# Solution adapted from https://www.datacamp.com/community/tutorials/exploratory-data-analysis-python

# importing pandas package 
import pandas as pd 
  
# making data frame from csv file  
data = pd.read_csv("iris.csv") 

# Filter data to Petal length < 2?
a = data.query('petal_length < 2')

# display
print(a)