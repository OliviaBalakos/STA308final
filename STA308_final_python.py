#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 18:31:25 2022
STA308 final

@author: Oliviabalakos
"""
#####################################
## The following is a display of data wrangling 
## of gas prices by Census regions. 
## The final table will output 
## a 4x4 table with the four census regions 
## and their corresponding 
## mean percent increase between Diesel and Regular, 
## the coefficient of variation of the percent increase, 
## and the standard deviation of the percent increase.
#%%
import pandas as pd
GasPrices = pd.read_csv("https://tjfisher19.github.io/data/gasoline_prices.csv")
StateCodes = pd.read_csv("https://tjfisher19.github.io/data/state_abb_codes.csv")
CensusRegions = pd.read_csv("https://tjfisher19.github.io/data/censusRegions.csv")

GasPricesbyStateCode = GasPrices.merge(StateCodes, on="State")
GasPricesbyStateCode

## this gives the state code and the prices 

keeps = ["Code", "Regular", "Diesel"]

CodedNamedGasPrices = GasPricesbyStateCode[keeps] ## adapted from https://www.listendata.com/2015/06/r-keep-drop-columns-from-data-frame.html

## this is now the most updated, user-friendly df because 
## it has the code of the state and the regular and diesel mean corresponding prices 

GasPricesByRegion = CodedNamedGasPrices.merge(CensusRegions, left_on="Code", right_on="State") 
GasPricesByRegion 
## above was adapted from https://sparkbyexamples.com/pandas/pandas-merge-two-dataframes-on-multiple-columns/

## this output shows the region and corresponding state, with the diesel and regular mean gas prices 

## I also need to remove Washington, D.C. from the data. 



GasPricesByRegion_without_DC = GasPricesByRegion.loc[(GasPricesByRegion.Code!="DC")] 
## adapted from https://www.listendata.com/2019/07/how-to-filter-pandas-dataframe.html

## next step:
## need to sort the data
# group by region 
## Then, output a table with the mean percent increase between Diesel and Regular, 
## the coefficient of variation of the percent increase, 
## and the standard deviation of the percent increase.
#%%
#%%
GasPricesByRegion_without_DC.groupby("Region").agg("mean")
 
MeanOfGasPrices = GasPricesByRegion_without_DC.groupby("Region").mean()
print(MeanOfGasPrices)
  
GasPricesByRegion_without_DC.groupby("Region").std()



Mean = GasPricesByRegion_without_DC.assign(mean_pct_increase = 
                                    (GasPricesByRegion_without_DC.Diesel - 
                                     GasPricesByRegion_without_DC.Regular)/
                                    GasPricesByRegion_without_DC.Regular * 100).mean()
Mean
SD = GasPricesByRegion_without_DC.assign(std_pct_increase = 
                                  (GasPricesByRegion_without_DC.Diesel - 
                                   GasPricesByRegion_without_DC.Regular)/
                                  GasPricesByRegion_without_DC.Regular * 100).std()  
print(SD)
import numpy as np
cv = lambda x: np.std(x, ddof=1) / np.mean(x) * 100 
cv(GasPricesByRegion_without_DC)                                    
## above adapted from https://www.statology.org/coefficient-of-variation-in-python/ 

Table = GasPricesByRegion_without_DC.groupby("Region")["Diesel", "Regular"].mean()
print(Table)
Table.agg("sum")
 ## this provides the mean of diesel and reg per region 




GroupedData = GasPricesByRegion_without_DC.groupby("Region")["Diesel", "Regular"].agg(["mean", "std"])
print(GroupedData)
## this shows the mean and std for diesel -- then the mean and std for regular 



## Below is the aggregation and combination  



GasPricesByRegion_without_DC.assign(diesel_minus_reg_times_reg100 = 
                                    ((GasPricesByRegion_without_DC["Diesel"] -
                                    GasPricesByRegion_without_DC.Regular) /
                                    GasPricesByRegion_without_DC.Regular*100))







GasPricesByRegion_without_DC.groupby("Region")
## gives groupby() behind the scenes 




GasPricesByRegion_without_DC.groupby("Region")["Diesel"].mean()
Gas_with_mean_pct = GasPricesByRegion_without_DC.assign(mean_pct = 
                                    (GasPricesByRegion_without_DC.Diesel - 
                                    GasPricesByRegion_without_DC.Regular) /
                                    GasPricesByRegion_without_DC.Regular*100)
print(Gas_with_mean_pct)

Gas_Prices_Mean_Table = Gas_with_mean_pct.groupby("Region")["mean_pct"].mean()
print(Gas_Prices_Mean_Table)
### IT WORKS OMG!!!!! 


GasPricesByRegion_without_DC.groupby("Region")["Diesel"].std()
Gas_with_std_pct = GasPricesByRegion_without_DC.assign(std_pct = 
                                    (GasPricesByRegion_without_DC.Diesel - 
                                    GasPricesByRegion_without_DC.Regular) /
                                    GasPricesByRegion_without_DC.Regular*100)
print(Gas_with_std_pct)

Gas_Prices_Std_Table = Gas_with_std_pct.groupby("Region")["std_pct"].std()
print(Gas_Prices_Std_Table)


## Coeffiecent of variation or CV = std/mean 
## need to create a new colmn called CV_pct_increase 
## with the assign() opperator 
## cv = std/mean of each region 
cv = [7.925107/50.398801, 3.024418/55.816398, 3.885083/57.350560, 14.069044/ 33.309569]
print(cv)


GasPricesByRegion = CodedNamedGasPrices.merge(CensusRegions, left_on="Code", right_on="State") 


Final_Table = Gas_Prices_Std_Table.merge(Gas_Prices_Mean_Table, left_on="Region", right_on="Region")
Final_Table
New_table1 = Gas_Prices_Std_Table.to_frame().merge(Gas_Prices_Mean_Table.to_frame(), left_on="Region", right_on="Region")
print(New_table1)
### New_table1 is the most accurate version of the data currently... 
import pandas as pd 
cvdf = pd.DataFrame(cv, columns=["cv_pct"])
print(cvdf)
### adapted from https://www.geeksforgeeks.org/different-ways-to-create-pandas-dataframe/ 




## try column merge 
cv = [7.925107/50.398801, 3.024418/55.816398, 3.885083/57.350560, 14.069044/ 33.309569]
Newattempt_1030 = New_table1.assign(cv_pct=cv)
## adapted from https://sparkbyexamples.com/pandas/pandas-add-column-to-dataframe/amp/
Newattempt_1030
## it worked! 
#@# Newattemp_1030 outputs: 
    #####              std_pct   mean_pct    cv_pct
   # Region                                   
   # Midwest     7.925107  50.398801  0.157248
  # Northeast   3.024418  55.816398  0.054185
   # South       3.885083  57.350560  0.067743
  #  West       14.069044  33.309569  0.422372
  
#%%