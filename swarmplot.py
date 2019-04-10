# # Paul Caulfield, 2019
# My program reads in the iris.csv file and creates a swarmplot 
# A swarmplot is a scatterplot with non-overlapping points: ref https://seaborn.pydata.org/generated/seaborn.swarmplot.html

# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load iris data
iris = sns.load_dataset("iris")

# Construct iris plot
plt.figure(figsize=(15,10))
# Use subplot to compare different views of data side by side
f, (ax1, ax2, ax3, ax4) = plt.subplot(2,2,1)

ax1.sns.swarmplot(x="species", y="petal_length", data=iris)
ax2.sns.swarmplot(x="species", y="petal_width", data=iris)
ax3.sns.swarmplot(x="species", y="sepal_length", data=iris)
ax4.sns.swarmplot(x="species", y="sepal_width", data=iris)

# Show plot
plt.show()