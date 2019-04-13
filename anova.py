# # Paul Caulfield, 2019
# My program creates an ANOVA table in python using the Iris dataset. 

# Solution adapted from https://www.kaggle.com/morenoh149/iris-anova-table-python
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
df = pd.read_csv('iris.csv', delimiter=',')
# print(df.describe())
# print(df)
# iris_lm_one_categorical=ols('sepal_length ~ C(species)', data=df).fit() 
#Specify C for Categorical
# print(sm.stats.anova_lm(iris_lm_one_categorical, typ=2))

iris_lm=ols('sepal_length ~ C(species) + sepal_width + petal_length + petal_width', data=df).fit() 
#Specify C for Categorical
print(sm.stats.anova_lm(iris_lm, typ=2))