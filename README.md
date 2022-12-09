# STA308final
#### The two programs attached to this repo represent the same data handling, but reprodced and translated in both R and Python. 
#### The programs display data wrangling of gas prices by Census regions. 
#### The final table in each is an output of
#### a 4x4 table with the four Census regions and their corresponding 
#### - mean percent increase between Diesel and Regular, 
#### - standard deviation of the percent increase,
#### - and the coefficient of variation of the percent increase.

#### The coefficent of variation is the standard deviation divided by the mean, which is essentially a representation of how frequent the data is distribited throughout the dataset. 

#### The average percent differences between diesel and regular gas for the four regions showed some variety. 





| Functionality                               | In R               | In Python                   |
|---------------------------------------------|--------------------|-----------------------------|
| Reading in a CSV file           | library(tidyverse) df <- read_csv("the link)"            | Import pandas as pd df=pd.read_csv("the link")           |
| "Not" or getting rid of something | ! (i.e.), GasPricesByRegion %>% filter(Code !="DC")            | ! (i.e.), GasPricesByRegion.loc[(GasPricesByRegion.Code!="DC")]        |
| Merging two dataframes                   | df3 <- merge(df1, df2, by.x="x1", by.y="y1")                | df3 = df1.merge (df2,left_on= "x1", right_on= "y1") |
| Defines a function                          | name <- function() using {} to define | def = name_of_function(): using : to define     ||
| Creating a vector | V <- c(1,2,3)           | V=[1,2,3]       |
| View something in the console                    | glimpse() or print()                | print() |
| Group by some variable                          | Df %>% group_by(variable) | Df.groupby(variable)    |
| Find the type of variable | class(variable)           | variable.dtypes       |
| Summarise the data                    | df %>% summarise(sum=total_variable)                | df.agg("sum") |
| standard deviation                        | sd(x) | x.std()     |
| mean                       | mean(x) | x.mean()     |
| How to change a variable                        | mutate(x) | x.assign()     |

##### Throughout the course of STA308, the most helpful examples were the palmer penguins and pregnancy data. These two were robust examples of data handling and functions that were easy to follow in class and after class when reviewing notes for homework. Palmer penguins was useful when I needed to remember how to mutate a variable or which order I needed to use data handling verbs in such as filter(), select(), or group_by(). The pregnancy data was also helpful for understanding functions and the syntax for a loop. 
