# Project 2019 - Programming and Scripting
## Introduction

This document contains my research and investigation of the Iris Data Set. 

## Getting Started

I have created a GitHub Repository where you can access my project, its files, and all the versions of its files that Git saves. See link https://github.com/pcaulfie/pands-project

## Iris Flower Data Set - Overview / Short Summary
### About This Data Set
The Iris Flower Data Set also known as Fisher's or Andersons Data Set is a database containing the measurements of three related species of Iris; Iris setosa, Iris versicolor and Iris virginica (University of California, Irvine 1988).  
The data set is a record of the measurements taken from a sample of fifty flowers from each of the three species. The variables measured are; sepal length, sepal width, petal length and petal width. 
This data set has become an important reference ever since it was first cited by Fisher in his 1936 paper and it is cited regularly to this day, see UCI Machine Learning Repository.
Fisher (1936) outlines how the data set could be used to illustrate a model which could be used to identify patterns in the data. He interpreted the data, identifying variables could be used to predict which population class an object belonged to. 
The data was recorded by botanist Edgar Andersen (Anderson, Edgar 1936). 
### About Ronald Fisher
Ronald Fisher was a British mathematician, biologist and geneticist who is credited as the father of modern statistics (Allison, 2003). He prioneered the development of modern statistical techniques such as Analysis of Variance, Distribution Theory, Mathematical Likelihood and Estimation. He applied these techniques in the area of genetics where he developed theories on topics such as Natural Selection and Fiduciary Inheritance. He was also credited with establishing a new era in experiment design and statistical sampling techniques (Aldrich, 2003).

## Data Set
### Format
The data set is a comma-separated values (csv) file with 150 records (rows of data) and 5 fields (columns) named Sepal.Length, Sepal.Width, Petal.Length, Petal.Width, and Species. > CSV is a simple file format used to store tabular data, such as a spreadsheet or database. Files in the CSV format can be imported to and exported from programs that store data in tables, such as Microsoft Excel or OpenOffice Calc. (Computer Hope, 2018)
* Each record (row of data) is located on a separate line, delimited by a line break.
* The first line of the file is the header line. The header line contains the names of the 5 fields: Sepal.Length, Sepal.Width, Petal.Length, Petal.Width, and Species.
* The fields of data in the header line and each record (row) are delimited with a comma

### What do each of the columns look like
#### Statistical Properties
One is easy to seperate, 2 are not
#### Insert Table

## Investigation of the Data Set

### Importing The Data
In order to start exploring the Iris Dataset, the first step was to load in the data. I used the Pandas library (https://pandas.pydata.org/) to simplify the task and I used the standard conventions (Willems, 2017): 
* First you import the package as pd, 
* Next, you use the read_csv() function, 
* Then you pass the URL in which the dataset can be found. I chose to use the following URL as the source: https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/d546eaee765268bf2f487608c537c05e22e4b221/iris.csv
* Finally you add a header argument and delimiter to make sure that your data is read in correctly (pandas.pydata.org, 2019).
  * As the first row of the dataset contains the columns names, I did not need to pass a header argument, instead pandas infers that the     first line will contain the column names. 
  * Pandas defaults the delimiter as comma unless you are trying to read in a file in another format. 
### Basic Description of the Data 
Before I could begin to get insights into the dataset, I first needed to get to know the dataset. I began by getting a basic description of the data. I wanted some simple, easy-to-understand information on ther data, to give me a feel for the data. I thought it would be best to start with Mean, Min, Max and Standard Deviation. 

#### Max, Min, Mean, Standard Deviation
I used the describe() function to view some basic summary statistics. "This function returns the count, mean, standard deviation, minimum and maximum values and the quantiles of the data like percentile, mean, std etc." (Willems, K (2017). Here is an overivew of the program I wrote:
* First you import the package as pd, 
* Next, you use the read_csv() function, 
* Then you use the describe() function to get various summary statistics
* Finally you include the print function to display the results
Link to program : https://github.com/pcaulfie/pands-project/blob/master/describe.py
##### Results
![Summary Statistics](https://github.com/pcaulfie/pands-project/blob/master/describe.JPG)
##### Interpretation of Results
A quick look at the data shows that standard deviation of petal_length is greater than any of the other 3 variables. This is worth investigating further.

#### Research other ways to summarize the data set
#### Swarmplot
![alt text](https://github.com/pcaulfie/pands-project/blob/master/Swarmplot.png "Swarmplot")
Figure: ![Swarmplot - Iris Dataset](https://github.com/pcaulfie/pands-project/blob/master/swarmplot.py)
#### Scatterplot Matrix
![alt text](https://github.com/pcaulfie/pands-project/blob/master/Scatterplot%20Matrix.png "Scatterplot Matrix")
Figure: ![Scatterplot Matrix - Iris Dataset](https://github.com/pcaulfie/pands-project/blob/master/Scatterplot_Matrix.py)
#### Investigation of Python Packages using data set in their tutorials
#### Pandas - e.g scatter diagrams 
### Summary of Investigation at beginning or end?



## References
1. University of California, Irvine (1988) *Iris Plants Database* [Online] Available at: http://https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.names/ [Accessed 1 April 2019].
2. Fisher, R. A. (1936) *The use of multiple measurements in taxonomic problems* Annals of Eugenics, 7, Part II, 179–188. [Online] Available at doi:10.1111/j.1469-1809.1936.tb02137.x. [Accessed 1 April 2019]
3.Edgar Anderson (1936). *The species problem in Iris*. Annals of the Missouri Botanical Garden. 23 (3): 457–509. [Online] Available at: doi:10.2307/2394164. JSTOR 2394164.[Accessed 1 April 2019].
4. Computer Hope (2018) *How To Create A CSV File* [Online] Available at: https://www.computerhope.com/jargon/n/newline.htm [Accessed 1 April 2019].
5. Allison, L (2003) *Ronald Aylmer Fisher (1890-1962)* [Online] Available at: http://users.monash.edu/~lloyd/tildeImages/People/Fisher.RA/ [Accessed 13 April 2019]
6. Aldrich, J (2003:2018) *A Guide to R. A. Fisher* [Online] Available at: http://www.economics.soton.ac.uk/staff/aldrich/fisherguide/rafframe.htm [Accessed 13 April 2019]
7. Willems, K (2017) *Python Exploratory Data Analysis Tutorial* [Online] Available at: https://www.datacamp.com/community/tutorials/exploratory-data-analysis-python [Accessed 13 April 2019]
8. pandas.pydata.org (2019) *pandas: powerful Python data analysis toolkit* [Online] Available at: http://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html [Accessed 13 April 2019]

