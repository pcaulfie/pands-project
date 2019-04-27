# Paul Caulfield, 2019
# My program will use .info() function to gather information about the number of rows, columns, column data types, memory usage, etc.

# Solution adapted from https://www.datacamp.com/community/tutorials/categorical-data and https://www.geeksforgeeks.org/python-pandas-dataframe-info/


# importing pandas as pd 
import pandas as pd 
  
# Creating the dataframe  
df = pd.read_csv("iris.csv") 

# display results of .info() function
print(df.info())