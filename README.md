# STA308final
#### The two programs attached to this repo represent the same data handling, but reprodced and translated in both R and Python. 
#### The programs display data wrangling of gas prices by Census regions. 
#### The final table in each is an output of
#### a 4x4 table with the four Census regions and their corresponding 
#### mean percent increase between Diesel and Regular, 
#### standard deviation of the percent increase,
#### and the coefficient of variation of the percent increase.

#### The coefficent of variation is the standard deviation divided by the mean, which is essentially a representation of how frequent the data is distribited throughout the dataset. 

##### For this particular prompt, the results of the gas prices 





| Functionality                               | In R               | In Python                   |
|---------------------------------------------|--------------------|-----------------------------|
| Reading in a CSV file           | library(tidyverse) df <- read_csv("the link)"            | Import pandas as pd df=pd.read_csv("the link")           |
| "Not" or getting rid of something | ! (i.e.), GasPricesByRegion %>% filter(Code !="DC")            | ! (i.e.), GasPricesByRegion.loc[(GasPricesByRegion.Code!="DC")]        |
| Merging two dataframes                   | df3 <- merge(df1, df2, by.x="x1", by.y="y1")                | df3 = df1.merge (df2,left_on= "x1", right_on= "y1") |
| Defines a function                          | name <- function() | def name_of_function():     |

