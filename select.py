# Paul Caulfield, 2019
# My program reads in the iris.

# importing pandas package 
import pandas as pd 
  
# making data frame from csv file  
df = pd.read_csv("iris.csv") 

# Filter data where Petal length < 2?
result = df.query('species == setosa')
 

#a = df['species'] == "setosa"

print(result)