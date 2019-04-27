# Paul Caulfield, 2019
# My program creates a 2-Way ANOVA table in python using the Iris dataset. 

# Solution adapted from https://www.kaggle.com/morenoh149/iris-anova-table-python
# Import the `pandas` library as `pd`
import pandas as pd
# Import the `statsmodels` library as `sm`
import statsmodels.api as sm
# Import OLS regression library
from statsmodels.formula.api import ols
# Load in the data with `read_csv()` then I pass the URL in which the data can be found. Column names are on the first row, so default is used. http://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
# adapted from https://www.datacamp.com/community/tutorials/exploratory-data-analysis-python
df = pd.read_csv("https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/d546eaee765268bf2f487608c537c05e22e4b221/iris.csv", delimiter=',')

# create a 2 dimensional array using species as categorical and sepal length + sepal width as variables (dimensions)
iris_lm=ols('sepal_length ~ C(species) + sepal_width', data=df).fit() 
# Specify C for Categorical
print("")
print("2 Way Anova - Sepal Length + Sepal Width")
print(sm.stats.anova_lm(iris_lm, typ=2))

iris_lm2=ols('sepal_length ~ C(species) + sepal_width + petal_length', data=df).fit() 
# Specify C for Categorical
print("")
print("2 Way Anova - Sepal Length + Sepal Width + Petal Length")
print(sm.stats.anova_lm(iris_lm2, typ=2))

iris_lm3=ols('sepal_length ~ C(species) + sepal_width + petal_length + petal_width', data=df).fit() 
# Specify C for Categorical
print("")
print("2 Way Anova - Sepal Length + Sepal Width + Petal Length + Petal Width")
print(sm.stats.anova_lm(iris_lm3, typ=2))