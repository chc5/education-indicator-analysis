# education-indicator-analysis
### CSC 59970
**Michael Li, Melvin Cherian, Chieh-Huang-Chen**

## About
Our Education Indicator Analysis project explores direct and indirect correlations of educational attainment in countries and create a model that predicts future growth in educational attainment in countries based on these correlations. We will also look into government spending on education and life expectancy for the country's population that are known to have a direct impact in increasing educational attainment for the population.

## Gathering Our Data
We used the Human Development Dataset from the United Nations that can be found [here](hdr.undp.org/en/data). This dataset have data on many human development indicators for each country since the 1990s.
We performed some initial analysis on the dataset to pinpoint some noteworthy categories. 

## Cleaning and Filling out our Missing Data
The dataset itself had a lot of missing data on the dataset. So we decided to remove rows that only had at most two data points per row. From there, we also decided to fill the missing data with predicted values from a simple regression model of the indicators versus the year because if we removed all the rows with NaN, there wouldn't be any data left to work on. We also thought about replacing the missing data with the mean of the rows, but using a regression model worked better for us because it was more accurate later on for the entire model.

## Selecting our Indicators as our Predictors
First, we removed all the indicators that didn't have a direct correlation to the Education Index based on the coefficient of determination (R^2). From there, we had to resolve the issue of multicollinearity between the indicators in order to build our linear regression model. We then grouped these indicators together based on the categories that the United Nations provided on the dataset. Since they were grouped by context, it also means that these indicators aren't closely correlated with each other either. Our predicators are selected by picking the highest correlated indicator from each group for our model.

## Creating our Model
Our model uses a multiple linear regression model that uses the predictors we gathered previously from hundreds of indicators per country. We used a time-split cross-validation to determine how well this model would perform for future years by using the past 5 years as our test set and the rest of the set as our training set. We used the standard error as our scoring guideline and compete how well this model does compared to a simple linear regression model between Education Index and year. However, only 40 out of 187 countries that uses our model won against a simple model. We tried to use Ridge and Lasso Regression to improve the accuracy of our model because these two regression model would help in regularizing our model against multicollinearity. Our attempt failed because there wasn't much improvement compared to a normal multiple linear regression model. 

## Analyzing Correlations between Government Spending and Education
We decided to examine government spending on education closely because we strongly expect that an increase in government spending on education would increase the amount of school and learning resources in the country. This would also lead to a higher quality of education for the population and increase the educational attainment and success for everyone in the country. Based on our hypothesis, we performed analytics and see how much impact would government spending affect the education in the country.

## Analyzing Correlations between Health and Education
We also decided to examine the relationship between health and education of the nation because we speculate that a long life expectancy would lead to more time spent on education for the population. The additional amount of time spent on education would also lead to an overall increase in a higher educational attainment for a country. Based on our assumption, we analyzed this effect on education on several countries and how this effect would vary based on different life expectancies in different countries.
 
