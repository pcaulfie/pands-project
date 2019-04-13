# # Paul Caulfield, 2019
# My program aims to identify the pairwise correlation of all columns in the Iris dataset. 

# Solution adapted from https://www.geeksforgeeks.org/python-pandas-dataframe-corr/

# importing pandas as pd 
import pandas as pd 
  
# Making data frame from the csv file 
df = pd.read_csv('iris.csv', delimiter=',') 
# To find the correlation among 
# the columns using pearson method 
print(df.corr(method ='pearson'))


