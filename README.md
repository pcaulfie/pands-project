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
### Who is Ronald Fisher

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

### Read in the csv file - preferably via url 
### Summarize Data
#### Max, Min, Mean, Standard Deviation
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

