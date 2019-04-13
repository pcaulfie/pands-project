# # Paul Caulfield, 2019
# My program creates an ANOVA table in python using the Iris dataset. 

# Solution adapted from https://www.kaggle.com/morenoh149/iris-anova-table-python
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
df = pd.read_csv('iris.csv', delimiter=',')
print(df.describe())
# print(df)

