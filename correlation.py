# # Paul Caulfield, 2019
# My program aims to identify the pairwise correlation of all columns in the Iris dataset. 

# Solution adapted from https://www.geeksforgeeks.org/python-pandas-dataframe-corr/

# importing pandas as pd 
import pandas as pd 
  
# Making data frame from the csv file 
df = pd.read_csv('iris.csv', delimiter=',') 
# Use corr() function to find the correlation among the columns using pearson method 
print("")
print("Pearson Method")
print(df.corr(method ='pearson'))

# Use corr() function to find the correlation among the columns using kendall method 
print("")
print("Kendall Method")
print(df.corr(method ='kendall'))