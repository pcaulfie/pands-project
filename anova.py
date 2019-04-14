# # Paul Caulfield, 2019
# My program creates an ANOVA table in python using the Iris dataset. 

# Solution adapted from https://www.kaggle.com/morenoh149/iris-anova-table-python
# Import the `pandas` library as `pd`
import pandas as pd
# Import the `pandas` library as `pd`
import statsmodels.api as sm
#
from statsmodels.formula.api import ols
## Load in the data with `read_csv()` then I pass the URL in which the data can be found. Column names are on the first row, so default is used. http://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
# adapted from https://www.datacamp.com/community/tutorials/exploratory-data-analysis-python
df = pd.read_csv("https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/d546eaee765268bf2f487608c537c05e22e4b221/iris.csv", delimiter=',')

print(df.describe())

# iris_lm_one_categorical=ols('sepal_length ~ C(species)', data=df).fit() 
#Specify C for Categorical
# print(sm.stats.anova_lm(iris_lm_one_categorical, typ=2))

iris_lm=ols('sepal_length ~ C(species) + sepal_width + petal_length + petal_width', data=df).fit() 
# Specify C for Categorical
print(sm.stats.anova_lm(iris_lm, typ=2))