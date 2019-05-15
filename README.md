# education-indicator-analysis
### CSC 59970
**Michael Li, Melvin Cherian, Chieh-Huang-Chen**

## Gathering Our Data
After choosing our topic, we began looking for datasets.
We found that the United Nations has been gathering data on many human development indicators for each country since the 1990s.
We performed some initial analysis on the dataset to pinpoint some noteworthy categories. 

## How we cleaned the data
First we read the data. 
We were interested in the values at each year so we dropped the last column.
There were many cells that possess a value of nan which means that that entry was absent.
A large number of nan cells in a row would mean a lack of data over time. 
We decided to remove the indicators that possess two or fewer datapoints in each row.

## How we gathered our indicators
First we looked at the correlations of the indicators with Education Index.
Then we selected the indicators with the highest coorelation to education Index.
Using those indicators we looked at the indicators that appeared most frequently in each country.
We found that there were approximately 78 predicators that could possibly predict the education index for each individual country.

## How we gathered non-collinear indicators
Many of these 78 predictors were collinear so we grouped the indicators into different categories.
After that we took the highest correlated indicator from each griyo and used it for our model.
Through this method, we had approximately 21 predicators left which were all non-colinear with each other.

## How we created the model
We created several linear regression models by using the predictors that we found earlier.
We determined that our model worked by training our data with values from 1990 to 2011 and testing the model with values from 2012 to the present.
Using cross-validation allowed us to see that our model performed better than a regular linear regression model for 89 our of the 186 countries.

## Why did we take a look at government spending
We decided to examine government spending on education closely because theoretically, a larger amount spent would mean more schools or more resources for schools.
This would lead to a higher quality education for the people and would allow them to have greater educational success later on. We wanted to see whether this was
true when analyzing the data and to what degree the effect is if there was any at all.

## Why did we take a look at health
We decided to examine health because in theory, a longer life expectancy would mean that people would be more willing to seek out education. This would 
lead to a more educated population as a whole and would allow a country to have a overall higher education index. We wanted to see the effect on several
different countries and how the results vary from different life expectancies.
 
