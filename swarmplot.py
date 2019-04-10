# # Paul Caulfield, 2019
# My program reads in the iris.csv file and creates a swarmplot 
# A swarmplot is a scatterplot with non-overlapping points: ref https://seaborn.pydata.org/generated/seaborn.swarmplot.html

# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load iris data
iris = sns.load_dataset("iris")

# Construct iris plot
sns.swarmplot(x="species", y="sepal_length", data=iris)

# Show plot
plt.show()