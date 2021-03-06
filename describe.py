# Paul Caulfield, 2019
# My program generates summary statistics used to describe the dataset in simple terms. 

# Solution adapted from https://www.datacamp.com/community/tutorials/exploratory-data-analysis-python
# Import the `pandas` library as `pd`
import pandas as pd

## Load in the data with `read_csv()` then I pass the URL in which the data can be found. Column names are on the first row, so default is used. http://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
# adapted from https://www.datacamp.com/community/tutorials/exploratory-data-analysis-python
df = pd.read_csv("https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/d546eaee765268bf2f487608c537c05e22e4b221/iris.csv", delimiter=',')
# display results
print(df.describe())