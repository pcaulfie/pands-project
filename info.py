# Paul Caulfield, 2019
# My program will gather some information about different columns in the dataset

# Soulution adapted from https://www.datacamp.com/community/tutorials/categorical-data and https://www.geeksforgeeks.org/python-pandas-dataframe-info/


# importing pandas as pd 
import pandas as pd 
  
# Creating the dataframe  
df = pd.read_csv("iris.csv") 

print(df.info())