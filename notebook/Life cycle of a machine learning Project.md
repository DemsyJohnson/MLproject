# Student Performance Indicator



#### Life Cycle of Machine learning Project





* Understanding the Problem Statement
* Data Collection
* Data Checks to Perform
* Exploratory data analysis
* Data Pre-Processing
* Model Training
* Choose best model





1)Problem Statement



* This project understands how the student's performance( test scores) is affected by other variables such as Gender, Ethnicity, Parental level of education, Lunch and Test preparation course\\

2)Data Collection

* Data source -
* The data consists of 8 columns and 1000 rows



2.1) Import Data and Required Packages





Importing Pandas, NumPy, Matplotlib, Seaborn and Warnings Library.



Import the CSV Data as Pandas DataFrame



Show Top 5 Records



Shape of the dataset



## 2.2 Dataset information





* gender: sex of students - > (Male/Female)
* race/ethnicity: ethnicity of students -> (Group A, B, C, D, E)
* parental level of education: parents final education -> (bachelor's degree, some college, master's degree, associate's degree, high school)
* lunch: having lunch before test ( standard or free/reduced)
* test preparation course: complete or not complete before test
* math score
* reading score
* writing score





3\. Data Checks to Perform



* Check Missing values
* Check Duplicate
* Check data type
* Check the number of unique values of each column
* Check statistics of data set
* Check various categories present in the different categorical column



3.1 Check Missing values



There are no missing values in the data set







3.2 Check Duplicates



There are no duplicates in data set





3.3 Check data types

df.info()





3.4 Checking the number of unique values of each column

 df.unique()





3.5 Check statistics of data set

 df.describe()





### Insight



* From above description of numerical data, all means are very close to each other - between 66 and 68.05;
* All standard deviations are also close - between 14.6 and 15.19;
* while there is a minimum score 0 for math, for writing minimum is much higher = 10 and for reading myet higher = 17





3.7  Exploring Data

df.head()

categories in 'gender' variables:     \['female' 'male']

categories in 'race\_ethnicity' variables:





3.8 Adding columns for "Total Score" and "Average"



Insights

* From above values we get students have performed the worst in Maths
* Best Performance in reading section





4\. Exploring Data (Visualization)





4.1 Visualize average score distribution to make some conclusion.



* Histogram
* Kernel Distribution Function (KDE)



4.1.1 Histogram \& KDE



Insights



* Female students tend to perform well than male students







Insights



* Standard lunch helps perform well in games
* Standard lunch helps perform well in exams be it a male or female.





Insights

* In general parent's education don't help student perform well in exam.
* 2nd plot shows that parent's whose education is of associate's degree or master's , their male child tend to perform well in exam
* 3rd plot we can see there is no effect of parent's education on female students.







Insights

* Students of group A and group B tends to perform poorly in exam
* Students of group A and group B tends to perform poorly in exam irrespective of whether they are male or female







4.2 Maximum score of students in all three subjects



Insights

* From the above three plots, its clearly visible that most of the students score in between 60-80 in Maths whereas in reading and writing most of them score from 50-80





4.3 Multivariate analysis using pieplot



Insights

* Number of Male and Female students is almost equal
* Number of students are greatest in Group C
* Number of students who have started lunch are greater
* Number of students who have not enrolled in any test preparation course is greater.
* Number of students whose parental education is "some College" is greater followed by "Associate's Degree"





4.4 Feature Wise Visualization



4.4.1 GENDER COLUMN



* How is distribution of Gender?
* Does gender has any impact on student's performance?





UNIVARIATE ANALYSIS ( How is distribution of Gender ?)



Insights

* On an average females have a better overall score than men
* Whereas males have scored higher in Maths





4.4.2   RACE/ETHNICITY COLUMN



* How is Group wise distribution?
* Is Race/Ethnicity has any impact on student's performance?





UNIVARIATE ANALYSIS ( How is Group wise distribute ?)



Insights 

* Most of the student belonging from group C/ group D 
* lowest number of students belong to group A





BIVARIATE ANALYSIS (Is Race/Ethnicity has any impact on student's performance ?)



Insights 

* Group E students have scored the highest marks
* Group A students have scored the lowest marks
* Students from a lower socioeconomic status have a lower avg in all course subjects.







4.4.3 PARENTAL LEVEL OF EDUCATION COLUMN



* What is educational background of student's parent ?
* Is parental education has any impact on student's performance?







UNIVARIATE ANALYSIS ( What is educational background of student's parent?)



Insights 

* Largest number of parents are from some college



BIVARAIATE ANALYSIS (Is parental education has any impact on student's performance?)



Insights









































q



































&nbsp;

