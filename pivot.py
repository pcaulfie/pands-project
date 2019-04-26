# Paul Caulfield, 2019
# My program generates a pivot table to display dataset.

# Solution adapted from https://towardsdatascience.com/python-for-data-science-from-scratch-part-ii-e4dd4b943aba
# Import the `pandas` library as `pd` and 'numpy' as np
import pandas as pd
import numpy as np

## Load in the data with `read_csv()` then I pass the URL in which the data can be found. Column names are on the first row, so default is used. http://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
# adapted from https://www.datacamp.com/community/tutorials/exploratory-data-analysis-python
df = pd.read_csv("https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/d546eaee765268bf2f487608c537c05e22e4b221/iris.csv", delimiter=',')

#create a pivot tables
table = pd.pivot_table(df,values = ['petal_length','petal_width','sepal_length','sepal_width'], index=['species'],aggfunc=np.mean)
table2 = pd.pivot_table(df,values = ['petal_length','petal_width','sepal_length','sepal_width'], index=['species'],aggfunc=np.std)
# display results
print("Pivot Table - Mean")
print(table)
print("Pivot Table - Standard Deviation")
print(table2)
