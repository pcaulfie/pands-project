# # Paul Caulfield, 2019
# My program reads in the iris.csv file and creates a swarmplot 
# A swarmplot is a scatterplot with non-overlapping points: ref https://seaborn.pydata.org/generated/seaborn.swarmplot.html

# Import necessary libraries adapted from https://www.datacamp.com/community/tutorials/seaborn-python-tutorial#load
# Matplotlib still underlies Seaborn, so that is why it is imported here; https://www.datacamp.com/community/tutorials/seaborn-python-tutorial#load
import seaborn as sns
import matplotlib.pyplot as plt
# Switch to seaborn defaults, using the set() function. https://seaborn.pydata.org/tutorial/aesthetics.html
sns.set()
# Set context to `"paper"` control the plot elements. Paper is the smallest of the four preset contexts,https://seaborn.pydata.org/tutorial/aesthetics.html
sns.set_context("paper")
# Load iris data  as "df" from built-in Seaborn dataset located at https://github.com/mwaskom/seaborn-data/blob/master/iris.csv
iris = sns.load_dataset("iris")
# Construct iris swarmplot 
# define the area of the plot, ie 15 x 10 inchs) adapted from https://www.kaggle.com/lalitharajesh/iris-dataset-exploratory-data-analysis/data
plt.figure(figsize=(15,10))
# Use subplot to compare different views of data side by side https://www.kaggle.com/lalitharajesh/iris-dataset-exploratory-data-analysis/data
# Plot subplot in grid 2 x 2 on Top Left
plt.subplot(2,2,1)
## Solution for single swarmplot adapted from https://www.datacamp.com/community/tutorials/seaborn-python-tutorial#load
sns.swarmplot(x="species", y="petal_length", data=iris)
# Plot subplot in grid 2 x 2 on Top Right
plt.subplot(2,2,2)
sns.swarmplot(x="species", y="petal_width", data=iris)
# Plot subplot in grid 2 x 2 on Bottom Left
plt.subplot(2,2,3)
sns.swarmplot(x="species", y="sepal_length", data=iris)
# Plot subplot in grid 2 x 2 on Bottom Right
plt.subplot(2,2,4)
sns.swarmplot(x="species", y="sepal_width", data=iris)
# Show plot
plt.show()