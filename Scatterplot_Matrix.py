# # Paul Caulfield, 2019
# My program reads in the iris.csv file and creates a scatterplot matrix.

# Import necessary libraries adapted from https://www.datacamp.com/community/tutorials/seaborn-python-tutorial#load
# Matplotlib still underlies Seaborn, so that is why it is imported here; https://www.datacamp.com/community/tutorials/seaborn-python-tutorial#load
import seaborn as sns
import matplotlib.pyplot as plt


# Solution adapted from https://seaborn.pydata.org/examples/scatterplot_matrix.html#

# Seaborn does not have a default style, instead it comes with 5 preset styles, which must be called
# I am using seaborn themes: ticks, as it is commonly used to give extra structure to the plots https://seaborn.pydata.org/tutorial/aesthetics.html
sns.set(style="ticks")

# Load iris data  as "df" from built-in Seaborn dataset located at https://github.com/mwaskom/seaborn-data/blob/master/iris.csv
df = sns.load_dataset("iris")

# Construct iris scatterplot using pairplot function - adapted from https://seaborn.pydata.org/generated/seaborn.pairplot.html
sns.pairplot(df, hue="species", palette="husl", markers=["o", "s", "D"])
# Hue is used to display each species in a different color.
# Palette ="husl" used to change color palette to husl instead of default. ref: https://seaborn.pydata.org/tutorial/color_palettes.html
# markers=["o", "s", "D"] are used to display different markers for each level of the hue variable:

# show scatterplot
plt.show()