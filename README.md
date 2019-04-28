# Project 2019 - Programming and Scripting

## Introduction

This document contains my research and data analysis of the [Fisher's Iris Data Set](http://archive.ics.uci.edu/ml/datasets/Iris) using the Python programming language. 
![Iris Species](https://github.com/pcaulfie/pands-project/blob/master/iris-setosa.png) 

## Getting Started

I have created a [GitHub Repository](https://github.com/pcaulfie/pands-project) where you can access my project, its files, and the commit history.

## Iris Flower Data Set - Overview / Short Summary

### About This Data Set
The Iris Flower Data Set also known as Fisher's or Andersons Data Set is a database containing the measurements of three related species of Iris; Iris Setosa, Iris Versicolor and Iris Virginica (University of California, Irvine 1988).  
The data set is a record of the measurements taken from a sample of fifty flowers from each of the three species. The variables measured are; sepal length, sepal width, petal length and petal width. 
This data set has become an important reference ever since it was first cited by Fisher in his 1936 paper and it is cited regularly to this day, see UCI Machine Learning Repository (University of California, Irvine 1988).
Fisher (1936) outlines how the data set could be used to illustrate a model which could be used to identify patterns in the data. He interpreted the data, identifying variables could be used to predict which population class an object belonged to. 
The data was originally recorded by botanist Edgar Andersen (Anderson, Edgar 1936). 
### About Ronald Fisher
Ronald Fisher was a British mathematician, biologist and geneticist who is credited as the father of modern statistics (Allison, 2003). He pioneered the development of modern statistical techniques such as Analysis of Variance, Distribution Theory, Mathematical Likelihood and Estimation. He applied these techniques in the area of genetics where he developed theories on topics such as Natural Selection and Fiduciary Inheritance. He was also credited with establishing a new era in experiment design and statistical sampling techniques (Aldrich, 2003).
### Summary of Research
As mentioned above, the data set has been the subject of many studies, far to many in fact to mention. Here is a summary of the key findings from some of the research published on the data set.
* The data set contains  150 records, which can be grouped into 3 classes of 50 instances, each representing a species of iris plant. One class (Iris Setosa) is linearly separable from the other. The other 2 species (Iris Versicolor and Iris Virginica) are not linearly separable from each other (University of California, Irvine 1988).
* Santos, R (2018) proved that that petal length of the species setosa is shorter than the petal length of other species.  
* There is a high correlation between petal length and petal width (University of California, Irvine 1988) and (Santos 2018)
* Species has predictive power for sepal length (Rajesh 2018).
* Nichols (2014) wrote that "assertion that Petal.Length and Petal.Width are highly positively correlated is misleading. When looking at individual species, it transpires that the within-species correlation between between Petal.Length and Petal.Width is much
weaker". 

## Data Set

### Iris Dataset
In Appendix 1, I have included a table displaying the Iris Dataset. I created this table as follows:
* I used a program called csvtomd to convert the iris.csv into markdown table called iris.md [(Lewis 2018)](https://github.com/mplewis/csvtomd).
* Before I could run this program, I first had to install the csvtomd program using the command: pip3 install csvtomd at the CLI.
* Next, I ran the command on the command line: csvtomd iris.csv > iris.md .
![Command Line](https://github.com/pcaulfie/pands-project/blob/master/csvtomd%20command.JPG)
* Then I pushed the iris.md file to the repository.
* I opened iris.md in the repository and clicked on the "Raw" button, which opened an unprocessed version of the iris.md file. 
* I then copied the raw table and pasted it into the readme, see Appendix 1 or click on this link: [iris](iris.md).

### Format
The data set is a comma-separated values (csv) file with 150 records (rows of data) and 5 fields (columns) named sepal_length, sepal_width, petal_length, petal_width, and species. CSV is a simple file format used to store tabular data, such as a spreadsheet or database. Files in the CSV format can be imported to and exported from programs that store data in tables, such as Microsoft Excel or OpenOffice Calc (Computer Hope, 2018).
* Each record (row of data) is located on a separate line, delimited by a line break.
* The first line of the file is the header line. The header line contains the names of the 5 fields: sepal_length, sepal_width, petal_length, petal_width, and species.
* The fields of data in the header line and each record (row) are delimited with a comma.

### Summary of Dataframe
I used the Pandas dataframe.info() function to get a quick overview of the dataset. This overview is useful to have when conducting exploratory data analysis (Ranjan, 2018). I used the dataframe.info() function to gather information about the number of rows, columns, column data types, memory usage, etc. I adapted the program from the following references; [Pathak, M (2018)](https://www.datacamp.com/community/tutorials/categorical-data) and [Ranjan, S (2018)](https://www.geeksforgeeks.org/python-pandas-dataframe-info/).
* Step 1: import pandas as pd,
* Step 2: Create the dataframe df = pd.read_csv("iris.csv"),
* Step 3: Print the full summary of the dataframe with null count excluded,
* Link to program: [Info.py](https://github.com/pcaulfie/pands-project/blob/master/info.py)
#### Table 1. Overview of Dataset
![info](https://github.com/pcaulfie/pands-project/blob/master/info.JPG)
#### Interpretation of Results
* The dataframe rangeindex = 150 which means that it contains 150 rows which are indexed beginning with 0 for first row and ending with 149 for last row.
* The dataframe contains 5 columns.
* 4 columns (sepal_length, sepal_width, petal_length, petal_width) contain floating point (decimal) numbers in the format float64. Float 64 is defined as by Scipy (2008-2009) as "Double precision float: sign bit, 11 bits exponent, 52 bits mantissa".
* 1 column (species) contains dtype = object which is used used to represent "string" or text fields.

### Data Type
The data set is made up of two data types: categorical and continous data.

* Categorical Data: This data usually has a limited or fixed, number of possible values, stored as string values which are used to describe some traits of the observations, for example gender or age group (Pathak 2018). In the iris dataset, the column "species" represents categorical data, as it has a fixed number of values: setosa, versicolor or virginica. Since there is no order to the data, this data can also be described as nominal data as opposed to ordinal data which has an order, scale or ranking associated with them, for example; economic class or Likert Scale.
* Continuous Data: Pathak (2018) describes continuous data as "numeric variables that have an infinite number of values between any two values". Examples of continuous data are, temperature, height, weight. In the iris dataset, the columns sepal_length, sepal_width, petal_length, petal_width represents continuous data.

## Investigation of the Data Set

### Importing the Data
I used the [Pandas library](https://pandas.pydata.org/) as it simplifies the task of importing the data (Willems, Mar-2017): 
* First you import the Pandas package as pd, 
* Next, you use the read_csv() function, 
* Then you pass the URL in which the dataset can be found. I used the following [URL](https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/d546eaee765268bf2f487608c537c05e22e4b221/iris.csv)
* Finally, you add a header argument and delimiter to make sure that your data is read in correctly (pandas.pydata.org, 2019).
  * As the first row of the dataset contains the columns names, I did not need to pass a header argument, instead pandas infers that the     first line will contain the column names. 
  * Pandas defaults the delimiter as comma unless you are trying to read in a file in another format. 

### Basic Description of the Data 
Before I could get insights into the dataset, I needed to get to know the dataset. I began by getting a basic description of the data. I wanted some simple, easy-to-understand information on the data, to give me a feel for the data. I thought it would be best to start with Mean, Min, Max and Standard Deviation. 

#### Max, Min, Mean, Standard Deviation
I used the describe() function to view some basic summary statistics. "This function returns the count, mean, standard deviation, minimum and maximum values and the quantiles of the data like percentile, mean, std etc." (Willems, Mar-2017). Here is an overview of the program I wrote which was adapted from [(Willems, Mar-2017)](https://www.datacamp.com/community/tutorials/exploratory-data-analysis-python).
* First you import the package pandas as pd, 
* Next, you use the read_csv() function, 
* Then you use the describe() function to get various summary statistics,
* Finally, you include the print function to display the results.
* Link to program: [Describe.py](https://github.com/pcaulfie/pands-project/blob/master/describe.py)
##### Table 2. Summary Statistics
![Summary Statistics](https://github.com/pcaulfie/pands-project/blob/master/describe.JPG)
##### Interpretation of Results
* A quick look at the data shows that standard deviation of petal_length is greater than any of the other 3 variables. This is worth investigating further in case there are any outliers.
* This results for Max, Min, Mean, Standard Deviation are the same as the results published by [University of California, Irvine (1988)](https://github.com/pcaulfie/pands-project/blob/master/UCI%20Results.JPG).

#### Querying the Data
Santos, R (2018) proved that that petal length of the species setosa is shorter than the petal length of other species.  I want to investigate this further, to see how many rows of data would have a petal length less than 1 standard deviation from the mean. The mean is 3.75cm and the standard deviation is 1.76, so I decided to check how many rows of data had a petal length less than 2. Here is an overview of the program I wrote adapted from [(Bhutanyi 2019)](https://www.geeksforgeeks.org/python-filtering-data-with-pandas-query-method/):
* First you import the package pandas as pd, 
* Next you make the data frame from the iris.csv file ,
* Then you use the query function to filter the data frame for Petal length < 2,
* The I modified which columns would be displayed using df.iloc function,
* The final step is to display the results.
* Link to program: [Test.py](https://github.com/pcaulfie/pands-project/blob/master/test.py)
##### Query Results
See Appendix 2 or clink on the following link to view the results of the query, [test results](test.txt).
##### Interpretation of Results
It is clear from the results that all the iris setosa samples have a petal length less than 2. This is significant as this is more than one standard deviation from the mean. If the species setosa differs significantly for one variable (petal length), the next step would be to test the other 3 variables, petal width, sepal length and sepal width. 

#### Pivot Table
I needed a quick way to summarize the data and sort the results by species to see if the initial findings about iris setosa are backed up I also wanted to test the other variables, to see if there are any other significant patterns in the data. I decided to use a pivot table to summarize the data. I adapted my program from [Yadav (2019)](https://towardsdatascience.com/python-for-data-science-from-scratch-part-ii-e4dd4b943aba). 
* First you import the package pandas as pd, and numpy as np,
* Next, you use the read_csv() function, 
* Then you use create the pivot tables, by selecting the values you want to display and the index field (species) and what aggfunc you wish to apply to aggregate the data i.e. mean and standard deviation,
* Finally, you include the print function to display the results and titles for each pivot table.
* Link to program: [Pivot.py](https://github.com/pcaulfie/pands-project/blob/master/pivot.py)
##### Table 3. Pivot Table
![Pivot Table](https://github.com/pcaulfie/pands-project/blob/master/pivot%20table.JPG)
##### Interpretation of Results
I was able to interpret the following from the pivot tables:
* The species setosa, differs significantly from other species, for the mean value of the variable's petal_length and petal_width.
* The species setosa, also differs significantly from other species, for the standard deviation value of the variable's petal_length and petal_width.
* The mean and standard deviation of the other 2 species seem to be positively correlated, suggesting that they may have some common characteristics. The species setosa, seem to share little in common with the species versicolor and virginica.

#### Scatterplot Matrix
Outliers are data that contain values that diverge significantly from most of your other data (Willems Mar-2017). I decided to make a scatter plot of to identify if there are any data points that don’t lie in the “expected” area of the plot. I used the [Seaborn library](http://seaborn.pydata.org/) to create the scatterplot . Seaborn has an impressive gallery and I decided to visualize the dataset using a scatterplot matrix. "A scatterplot matrix is a collection of scatterplots organized into a grid (or matrix). Each scatterplot shows the relationship between a pair of variables" (SAS Institute 2019).
Here is an overview of the program I wrote adapted from an example by Waskom [(2012-2018)](https://seaborn.pydata.org/examples/scatterplot_matrix.html#):
* First you import seaborn as sns, I also had to install seaborn via the anaconda prompt using command: pip install seaborn,
* Then you import matplotlib.pyplot as plt,
* Next you set the themes,
* Then you load iris data  as df from built-in Seaborn dataset l,
* The next step is to construct the iris scatterplot using pairplot function,
* You decide how to customize the way the plots are displayed using Hue, Palette and Markers etc.,
* Finally, you display the scatterplot using plt.show,
* Link to program: [Scatterplot_Matrix.py](https://github.com/pcaulfie/pands-project/blob/master/Scatterplot_Matrix.py)
##### Figure 1. Scatterplot Matrix
![Scatterplot Matrix](https://github.com/pcaulfie/pands-project/blob/master/Scatterplot%20Matrix.png)
##### Interpretation of Results
The first this you will notice when you look at the data is that the species setosa does not seem to have any relationship with the other two species. I was also able to interpret the following:
* There appears to be a weak relationship between sepal length and sepal width as the data points are not tightly packed together.
* Each pair of variables are positively correlated, when you exclude setosa. This means that as one variable increases, the other     variable tends to increase too.
* The data points in the scatterplot for petal length and petal width are the most tightly clustered along an imaginary line, suggesting a strong relationship.
* These findings could form the basis of some hypotheses which I will test later, including Analysis of Variance (ANOVA).

#### Correlation
The scatterplot above suggested that there may be a strong relationship between petal length and petal width. Interesting research from University of California, Irvine (1988) suggested a high correlation between petal length and petal width, see table 4.0 below.

##### Table 4.0 Summary Statistics: University of California, Irvine (1988)
![UCI 1988](https://github.com/pcaulfie/pands-project/blob/master/UCI%20Results.JPG)

I decided to use Pandas dataframe.corr() to find the pairwise correlation of all columns in the dataframe, this would prove my theory that petal length and petal width have a high correlation. I adapted my program from [(Ranjan, 2018)](https://www.geeksforgeeks.org/python-pandas-dataframe-corr/):
* Import pandas as pd,
* Create the data frame from the csv file,
* Use corr() function to find the correlation among the columns using pearson method,
* Use corr() function to find the correlation among the columns using kendall method,
* Print results,
* Link to program: [Correlation.py](https://github.com/pcaulfie/pands-project/blob/master/correlation.py)
##### Table 4.1 Pairwise Correlation Results
![Correlation](https://github.com/pcaulfie/pands-project/blob/master/Correlation%20-%20Pearson%20%26%20Kendall%20Method.JPG)
##### Interpretation of Results
* The correlation coefficient of a variable with itself is 1.
* The correlation coefficient of the following pairs of variables was strongest; petal_length & petal width, suggesting a strong positive relationship, when one variable increases, the other increases. 
  * This was the same finding published by University of California, Irvine (1988).
* The correlation coefficient of the following pairs of variables was next strongest; petal_length & sepal length, suggesting a strong positive relationship, ie as one variable increases, the other increases.
* The correlation coefficient of the following pairs of variables was smallest; sepal_length & sepal width, suggesting a very weak negative relationship between, when one variable increases, the other decreases.
* The correlation coefficient of the following pairs of variables was also weak; petal_width & sepal width, suggesting a very weak negative relationship between, when one variable increases, the other decreases.

#### Swarmplot Matrix
As there is a lot of overlapping data in a scatterplot, it can be difficult to get a feel for the distribution of values. There are many techniques to visualize the data to provide insights into the distribution of values, such as boxplots and violinplots. I decided to use swarmplots which is a scatterplot with non-overlapping points.
Here is an overview of the program I wrote adapted from an example by [Willems (Aug-2017)](https://seaborn.pydata.org/generated/seaborn.swarmplot.html):
* First you import seaborn as sns,
* Then you import matplotlib.pyplot as plt,
* Set context to paper control the plot elements. Paper is the smallest of the four preset contexts,
* Load iris data as df from built-in Seaborn dataset,
* Define the area of the plot,
* Use subplot to compare different views of data side by side ,
* Construct iris swarmplot,
* Show swarmplot.
* Link to program: [Swarmplot.py](https://github.com/pcaulfie/pands-project/blob/master/swarmplot.py)
##### Figure 2. Swarmplot Matrix
![Swarmplot](https://github.com/pcaulfie/pands-project/blob/master/Swarmplot.png "Swarmplot")
##### Interpretation of Results
I was able to interpret the following from the swarmplot:
* In the species setosa, the distribution is different for each of the 4 variables
* For each of the other two species, there appears to be a uniform distribution.
* The data points in the swarmplot for petal length and petal width are the most narrowly distributed, whereas the distribution of the other variables was much wider.
* These findings could form the basis of some hypotheses which I will test later, including Analysis of Variance (ANOVA).

#### Hypotheses Testing - One Way Anova
So far we have learned that the species setosa appears to be very different to the other two species. Also Rajesh (2018) concluded that species has predictive power for sepal length.

I needed to test this hypotheses. I used one-way analysis of variance (ANOVA) to determine whether there is any statistically significant differences between the species.
I adapted the solution from [(Moreno, 2019)](https://www.kaggle.com/morenoh149/iris-anova-table-python):
* Import the pandas library as pd, 
* Import the statsmodels library as sm,
* Import ols (OLS regression library),
* Load in the datato the dataframe with read_csv(),
* create a one dimensional array using species as categorical and sepal length as variable dimension,
* Specify C for Categorical - in this case I use species as the categorical,
* display results in Type 2 Anova dataframe,
* repeat steps for other 3 variables, so I can view results for all 4 variables at same time,
* Link to program: [Anova.py](https://github.com/pcaulfie/pands-project/blob/master/anova.py)
##### Table 5. One Way Anova
![Anova](https://github.com/pcaulfie/pands-project/blob/master/One%20Way%20Anova.JPG)
##### Interpretation of Results
* As the p value (Pr(>F) for all tests, is > 0.05 (α), the null hypothesis must be rejected. The null hypotheses states that the means of all species are all equal, this is usually defined as a significance level (denoted as α or alpha) of 0.05. This backs up the earlier findings that the differences between the species is statistically significant.

#### Hypotheses Testing - Two Way Anova
I used two-way analysis of variance (ANOVA) to determine whether there is any statistically significant differences between the species using a combination of variables. I adapted the solution from [(Moreno, 2019)](https://www.kaggle.com/morenoh149/iris-anova-table-python):
* Import the pandas library as pd, 
* Import the statsmodels library as sm,
* Import ols (OLS regression library),
* Load in the datato the dataframe with read_csv(),
* Create a multi-dimensional array using species as categorical and a combination of variables (dimension),
* Specify C for Categorical - in this case I use species as the categorical,
* Display results in Type 2 Anova dataframe,
* Repeat steps for other combination variables, so I can view results for all combinations at same time
* Link to program: [2wayanova.py](https://github.com/pcaulfie/pands-project/blob/master/2wayanova.py)
##### Table 5. Two Way Anova
![2WayAnova](https://github.com/pcaulfie/pands-project/blob/master/Two%20Way%20Anova.JPG)
##### Interpretation of Results
* As the p value (Pr(>F) for all 3 tests, is > 0.05 (α), the null hypothesis must be rejected. The null hypotheses states that the means of all species are all equal, this is usually defined as a significance level (denoted as α or alpha) of 0.05. This back up the earlier findings that the differences between the species is statistically significant.

### Summary of Investigation
* The evidence suggest that species setosa, differs significantly from other species. Evidence: 
  * the mean value of the variable's petal_length and petal_width.
  * the standard deviation value of the variable's petal_length and petal_width.
  * The mean and standard deviation of the other 2 species seem to be positively correlated, suggesting that they may have some common characteristics. 
 
* There is evidence to suggest that there is a high correlation between petal length and petal width. Evidence: 
  * The data points in the scatterplot for petal length and petal width are the most tightly clustered along an imaginary line, suggesting a strong relationship. 
  * The data points in the swarmplot for petal length and petal width are the most narrowly distributed, whereas the distribution of the other variables was much wider.
  * The correlation coefficient of the following pairs of variables was strongest; petal_length & petal width, suggesting a strong positive relationship, when one variable increases, the other increases. 


### Conculsions and Recommendations
As the species setosa, seem to share little in common with the species versicolor and virginica, the above results must be interpreted carefully. I agree with Nichols (2014) that you could draw different conclusions from the data set depending on what question you asked. For instance, if the species setosa was excluded from the dataset, entirely different conclusion could be drawn. If I were to undertake this study again, instead of trying to assess if pairs of variables are correlated, over all plants in the study, I would to study each species separately. 



## References
1. University of California, Irvine (1988) *Iris Plants Database* [Online] Available at: http://https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.names/ [Accessed 1 April 2019].
2. Fisher, R. A. (1936) *The use of multiple measurements in taxonomic problems* Annals of Eugenics, 7, Part II, 179–188. [Online] Available at doi:10.1111/j.1469-1809.1936.tb02137.x. [Accessed 1 April 2019]
3.Edgar Anderson (1936). *The species problem in Iris*. Annals of the Missouri Botanical Garden. 23 (3): 457–509. [Online] Available at: doi:10.2307/2394164. JSTOR 2394164.[Accessed 1 April 2019].
4. Computer Hope (2018) *How To Create A CSV File* [Online] Available at: https://www.computerhope.com/jargon/n/newline.htm [Accessed 1 April 2019].
5. Allison, L (2003) *Ronald Aylmer Fisher (1890-1962)* [Online] Available at: http://users.monash.edu/~lloyd/tildeImages/People/Fisher.RA/ [Accessed 13 April 2019]
6. Aldrich, J (2003:2018) *A Guide to R. A. Fisher* [Online] Available at: http://www.economics.soton.ac.uk/staff/aldrich/fisherguide/rafframe.htm [Accessed 13 April 2019]
7. Willems, K (Mar-2017) *Python Exploratory Data Analysis Tutorial* [Online] Available at: https://www.datacamp.com/community/tutorials/exploratory-data-analysis-python [Accessed 13 April 2019]
8. pandas.pydata.org (2019) *pandas: powerful Python data analysis toolkit* [Online] Available at: http://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html [Accessed 13 April 2019]
9. SAS Institute (2019) *Scatterplot Matrix" [Online] Available at: https://www.jmp.com/support/help/14-2/scatterplot-matrix.shtml [Accessed 14 April 2019]
10. Waskom, M (2012-2018) *Scatterplot Matrix* [Online] Available at:https://seaborn.pydata.org/examples/scatterplot_matrix.html# [Accessed 13 April 2019]
11. Willems, K (Aug-2017) *Python Seaborn Tutorial For Beginners* [Online] Available at: https://www.datacamp.com/community/tutorials/seaborn-python-tutorial#load [Accessed 13 April 2019]
12. Chris, user:354577 (2016) *what-do-raw-githubusercontent-com-urls-represent" [Online] Available at:https://raw.githubusercontent.com/pcaulfie/pands-project/master/iris.md [Accessed 26 April 2019]
13. Pathak, M (2018) *Handling Categorical Data in Python* [Online] Available at: https://www.datacamp.com/community/tutorials/categorical-data [Accessed 27 April 2019] 
14. Ranjan, S (2018) *Python | Pandas dataframe.info()* [Online] Available at:   https://www.geeksforgeeks.org/python-pandas-dataframe-info/ [Accessed 27 April 2019] 
15. Scipy Community, (2008-2009) *Data types*  [Online] Available at: https://docs.scipy.org/doc/numpy-1.13.0/user/basics.types.html [Accessed 27 April 2019] 
16. Rajesh, L (2018) *Iris Dataset - Exploratory Data Analysis* [Online] Available at: https://www.kaggle.com/lalitharajesh/iris-dataset-exploratory-data-analysis/data [Accessed 13 April 2019]
17. Yadav, R (2019) *Python for Data Science: From Scratch(Part II)* [Online] Available at: https://towardsdatascience.com/python-for-data-science-from-scratch-part-ii-e4dd4b943aba [Accessed 27 April 2019]
18. Lewis, M (2018) *Convert your CSV files into Markdown tables* [Online] Available at: https://github.com/mplewis/csvtomd [Accessed 27 April 2019]
19. Bhutanyi, K (2019) *Python | Filtering data with Pandas .query() method* [Online] Available at: https://www.geeksforgeeks.org/python-filtering-data-with-pandas-query-method/ [Accessed 26 April 2019]
20. Moreno, H (2019) *Iris dataset ANOVA table* [Online] Available at: https://www.kaggle.com/morenoh149/iris-anova-table-python/notebook [Accessed 13 April 2019]
21. Santos, R (2018) *Data Science Example - Iris dataset* [Online] Available at:  http://www.lac.inpe.br/~rafael.santos/Docs/R/CAP394/WholeStory-Iris.html [Accessed 13 April 2019]
22. Nicholls, R (2014) *Tutorial 2: Descriptive Statistics and Exploratory Data Analysis Answers Sheet* [Online] Available at: https://www2.mrc-lmb.cam.ac.uk/download/lectures/lmb_statistics_course_2014/tutorial_answers/Tutorial_2_Descriptive_statistics_and_exploratory_data_analysis_answers.pdf [Accessed 28 April 2019]
## Appendix

### Appendix 1
The Iris Dataset

sepal_length  |  sepal_width  |  petal_length  |  petal_width  |  species
--------------|---------------|----------------|---------------|------------
5.1           |  3.5          |  1.4           |  0.2          |  setosa
4.9           |  3            |  1.4           |  0.2          |  setosa
4.7           |  3.2          |  1.3           |  0.2          |  setosa
4.6           |  3.1          |  1.5           |  0.2          |  setosa
5             |  3.6          |  1.4           |  0.2          |  setosa
5.4           |  3.9          |  1.7           |  0.4          |  setosa
4.6           |  3.4          |  1.4           |  0.3          |  setosa
5             |  3.4          |  1.5           |  0.2          |  setosa
4.4           |  2.9          |  1.4           |  0.2          |  setosa
4.9           |  3.1          |  1.5           |  0.1          |  setosa
5.4           |  3.7          |  1.5           |  0.2          |  setosa
4.8           |  3.4          |  1.6           |  0.2          |  setosa
4.8           |  3            |  1.4           |  0.1          |  setosa
4.3           |  3            |  1.1           |  0.1          |  setosa
5.8           |  4            |  1.2           |  0.2          |  setosa
5.7           |  4.4          |  1.5           |  0.4          |  setosa
5.4           |  3.9          |  1.3           |  0.4          |  setosa
5.1           |  3.5          |  1.4           |  0.3          |  setosa
5.7           |  3.8          |  1.7           |  0.3          |  setosa
5.1           |  3.8          |  1.5           |  0.3          |  setosa
5.4           |  3.4          |  1.7           |  0.2          |  setosa
5.1           |  3.7          |  1.5           |  0.4          |  setosa
4.6           |  3.6          |  1             |  0.2          |  setosa
5.1           |  3.3          |  1.7           |  0.5          |  setosa
4.8           |  3.4          |  1.9           |  0.2          |  setosa
5             |  3            |  1.6           |  0.2          |  setosa
5             |  3.4          |  1.6           |  0.4          |  setosa
5.2           |  3.5          |  1.5           |  0.2          |  setosa
5.2           |  3.4          |  1.4           |  0.2          |  setosa
4.7           |  3.2          |  1.6           |  0.2          |  setosa
4.8           |  3.1          |  1.6           |  0.2          |  setosa
5.4           |  3.4          |  1.5           |  0.4          |  setosa
5.2           |  4.1          |  1.5           |  0.1          |  setosa
5.5           |  4.2          |  1.4           |  0.2          |  setosa
4.9           |  3.1          |  1.5           |  0.1          |  setosa
5             |  3.2          |  1.2           |  0.2          |  setosa
5.5           |  3.5          |  1.3           |  0.2          |  setosa
4.9           |  3.1          |  1.5           |  0.1          |  setosa
4.4           |  3            |  1.3           |  0.2          |  setosa
5.1           |  3.4          |  1.5           |  0.2          |  setosa
5             |  3.5          |  1.3           |  0.3          |  setosa
4.5           |  2.3          |  1.3           |  0.3          |  setosa
4.4           |  3.2          |  1.3           |  0.2          |  setosa
5             |  3.5          |  1.6           |  0.6          |  setosa
5.1           |  3.8          |  1.9           |  0.4          |  setosa
4.8           |  3            |  1.4           |  0.3          |  setosa
5.1           |  3.8          |  1.6           |  0.2          |  setosa
4.6           |  3.2          |  1.4           |  0.2          |  setosa
5.3           |  3.7          |  1.5           |  0.2          |  setosa
5             |  3.3          |  1.4           |  0.2          |  setosa
7             |  3.2          |  4.7           |  1.4          |  versicolor
6.4           |  3.2          |  4.5           |  1.5          |  versicolor
6.9           |  3.1          |  4.9           |  1.5          |  versicolor
5.5           |  2.3          |  4             |  1.3          |  versicolor
6.5           |  2.8          |  4.6           |  1.5          |  versicolor
5.7           |  2.8          |  4.5           |  1.3          |  versicolor
6.3           |  3.3          |  4.7           |  1.6          |  versicolor
4.9           |  2.4          |  3.3           |  1            |  versicolor
6.6           |  2.9          |  4.6           |  1.3          |  versicolor
5.2           |  2.7          |  3.9           |  1.4          |  versicolor
5             |  2            |  3.5           |  1            |  versicolor
5.9           |  3            |  4.2           |  1.5          |  versicolor
6             |  2.2          |  4             |  1            |  versicolor
6.1           |  2.9          |  4.7           |  1.4          |  versicolor
5.6           |  2.9          |  3.6           |  1.3          |  versicolor
6.7           |  3.1          |  4.4           |  1.4          |  versicolor
5.6           |  3            |  4.5           |  1.5          |  versicolor
5.8           |  2.7          |  4.1           |  1            |  versicolor
6.2           |  2.2          |  4.5           |  1.5          |  versicolor
5.6           |  2.5          |  3.9           |  1.1          |  versicolor
5.9           |  3.2          |  4.8           |  1.8          |  versicolor
6.1           |  2.8          |  4             |  1.3          |  versicolor
6.3           |  2.5          |  4.9           |  1.5          |  versicolor
6.1           |  2.8          |  4.7           |  1.2          |  versicolor
6.4           |  2.9          |  4.3           |  1.3          |  versicolor
6.6           |  3            |  4.4           |  1.4          |  versicolor
6.8           |  2.8          |  4.8           |  1.4          |  versicolor
6.7           |  3            |  5             |  1.7          |  versicolor
6             |  2.9          |  4.5           |  1.5          |  versicolor
5.7           |  2.6          |  3.5           |  1            |  versicolor
5.5           |  2.4          |  3.8           |  1.1          |  versicolor
5.5           |  2.4          |  3.7           |  1            |  versicolor
5.8           |  2.7          |  3.9           |  1.2          |  versicolor
6             |  2.7          |  5.1           |  1.6          |  versicolor
5.4           |  3            |  4.5           |  1.5          |  versicolor
6             |  3.4          |  4.5           |  1.6          |  versicolor
6.7           |  3.1          |  4.7           |  1.5          |  versicolor
6.3           |  2.3          |  4.4           |  1.3          |  versicolor
5.6           |  3            |  4.1           |  1.3          |  versicolor
5.5           |  2.5          |  4             |  1.3          |  versicolor
5.5           |  2.6          |  4.4           |  1.2          |  versicolor
6.1           |  3            |  4.6           |  1.4          |  versicolor
5.8           |  2.6          |  4             |  1.2          |  versicolor
5             |  2.3          |  3.3           |  1            |  versicolor
5.6           |  2.7          |  4.2           |  1.3          |  versicolor
5.7           |  3            |  4.2           |  1.2          |  versicolor
5.7           |  2.9          |  4.2           |  1.3          |  versicolor
6.2           |  2.9          |  4.3           |  1.3          |  versicolor
5.1           |  2.5          |  3             |  1.1          |  versicolor
5.7           |  2.8          |  4.1           |  1.3          |  versicolor
6.3           |  3.3          |  6             |  2.5          |  virginica
5.8           |  2.7          |  5.1           |  1.9          |  virginica
7.1           |  3            |  5.9           |  2.1          |  virginica
6.3           |  2.9          |  5.6           |  1.8          |  virginica
6.5           |  3            |  5.8           |  2.2          |  virginica
7.6           |  3            |  6.6           |  2.1          |  virginica
4.9           |  2.5          |  4.5           |  1.7          |  virginica
7.3           |  2.9          |  6.3           |  1.8          |  virginica
6.7           |  2.5          |  5.8           |  1.8          |  virginica
7.2           |  3.6          |  6.1           |  2.5          |  virginica
6.5           |  3.2          |  5.1           |  2            |  virginica
6.4           |  2.7          |  5.3           |  1.9          |  virginica
6.8           |  3            |  5.5           |  2.1          |  virginica
5.7           |  2.5          |  5             |  2            |  virginica
5.8           |  2.8          |  5.1           |  2.4          |  virginica
6.4           |  3.2          |  5.3           |  2.3          |  virginica
6.5           |  3            |  5.5           |  1.8          |  virginica
7.7           |  3.8          |  6.7           |  2.2          |  virginica
7.7           |  2.6          |  6.9           |  2.3          |  virginica
6             |  2.2          |  5             |  1.5          |  virginica
6.9           |  3.2          |  5.7           |  2.3          |  virginica
5.6           |  2.8          |  4.9           |  2            |  virginica
7.7           |  2.8          |  6.7           |  2            |  virginica
6.3           |  2.7          |  4.9           |  1.8          |  virginica
6.7           |  3.3          |  5.7           |  2.1          |  virginica
7.2           |  3.2          |  6             |  1.8          |  virginica
6.2           |  2.8          |  4.8           |  1.8          |  virginica
6.1           |  3            |  4.9           |  1.8          |  virginica
6.4           |  2.8          |  5.6           |  2.1          |  virginica
7.2           |  3            |  5.8           |  1.6          |  virginica
7.4           |  2.8          |  6.1           |  1.9          |  virginica
7.9           |  3.8          |  6.4           |  2            |  virginica
6.4           |  2.8          |  5.6           |  2.2          |  virginica
6.3           |  2.8          |  5.1           |  1.5          |  virginica
6.1           |  2.6          |  5.6           |  1.4          |  virginica
7.7           |  3            |  6.1           |  2.3          |  virginica
6.3           |  3.4          |  5.6           |  2.4          |  virginica
6.4           |  3.1          |  5.5           |  1.8          |  virginica
6             |  3            |  4.8           |  1.8          |  virginica
6.9           |  3.1          |  5.4           |  2.1          |  virginica
6.7           |  3.1          |  5.6           |  2.4          |  virginica
6.9           |  3.1          |  5.1           |  2.3          |  virginica
5.8           |  2.7          |  5.1           |  1.9          |  virginica
6.8           |  3.2          |  5.9           |  2.3          |  virginica
6.7           |  3.3          |  5.7           |  2.5          |  virginica
6.7           |  3            |  5.2           |  2.3          |  virginica
6.3           |  2.5          |  5             |  1.9          |  virginica
6.5           |  3            |  5.2           |  2            |  virginica
6.2           |  3.4          |  5.4           |  2.3          |  virginica
5.9           |  3            |  5.1           |  1.8          |  virginica

### Appendix 2
Results of Test.py
   species
0   setosa
1   setosa
2   setosa
3   setosa
4   setosa
5   setosa
6   setosa
7   setosa
8   setosa
9   setosa
10  setosa
11  setosa
12  setosa
13  setosa
14  setosa
15  setosa
16  setosa
17  setosa
18  setosa
19  setosa
20  setosa
21  setosa
22  setosa
23  setosa
24  setosa
25  setosa
26  setosa
27  setosa
28  setosa
29  setosa
30  setosa
31  setosa
32  setosa
33  setosa
34  setosa
35  setosa
36  setosa
37  setosa
38  setosa
39  setosa
40  setosa
41  setosa
42  setosa
43  setosa
44  setosa
45  setosa
46  setosa
47  setosa
48  setosa
49  setosa
