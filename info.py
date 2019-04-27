# Paul Caulfield, 2019
# My program will use .info() function to gather information about the number of rows, columns, column data types, memory usage, etc.

# Solution adapted from https://www.datacamp.com/community/tutorials/categorical-data and https://www.geeksforgeeks.org/python-pandas-dataframe-info/


# importing pandas as pd 
import pandas as pd 
  
# Creating the dataframe  
df = pd.read_csv("iris.csv") 

# # Print the full summary of the dataframe 
# with null count excluded source https://www.geeksforgeeks.org/python-pandas-dataframe-info/
print(df.info(verbose = True, null_counts = False))