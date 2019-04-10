# # Paul Caulfield, 2019
# My program reads in the iris.csv file and creates a scatterplot matrix.

# Import necessary libraries adapted from https://www.datacamp.com/community/tutorials/seaborn-python-tutorial#load
import seaborn as sns
import matplotlib.pyplot as plt

# Solution https://seaborn.pydata.org/examples/scatterplot_matrix.html#
sns.set(style="ticks")

# Load iris data from built-in Seaborn dataset
df = sns.load_dataset("iris")

# Construct iris scatterplot https://seaborn.pydata.org/generated/seaborn.pairplot.html
sns.pairplot(df, hue="species", palette="husl")
# Use a different color palette, taken from https://seaborn.pydata.org/tutorial/color_palettes.html

# show scatterplot
plt.show()