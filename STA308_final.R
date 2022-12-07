library(tidyverse)
GasPrices <- read_csv("https://tjfisher19.github.io/data/gasoline_prices.csv")
StateCodes <- read_csv("https://tjfisher19.github.io/data/state_abb_codes.csv")
CensusRegions <- read_csv("https://tjfisher19.github.io/data/censusRegions.csv")

GasPricesStateCode <-  merge(GasPrices, StateCodes, by=c("State"))
## this gives the state code and prices 

keeps <- c("Code", "Regular", "Diesel")

CodedNamedGasPrices <- GasPricesStateCode[keeps] ## adapted from https://www.listendata.com/2015/06/r-keep-drop-columns-from-data-frame.html

CodedNamedGasPrices 
## this is the most updated, user friednly DF because it 
## has the coded name of the state and the corresponding regular and diesel mean prices 

GasPricesByRegion <- merge(CodedNamedGasPrices, CensusRegions, by.x = "Code", by.y = "State")

GasPricesByRegion
glimpse(GasPricesByRegion)
## this DF shows the state code, and the corresponding region, mean diesel and mean regular gas prices 

##  first i need to remove Washington, D.C. from the DF 
GasPricesByRegion_without_DC <-
  GasPricesByRegion %>% 
  filter(Code !="DC")
## next step: 
## need to sort the data 
## group by region 

Aggregation <- GasPricesByRegion_without_DC %>% 
  group_by(Region) %>%
  summarise(pct_increase=((Diesel-Regular)/Regular * 100)) 

glimpse(Aggregation)
## aggregate mean by group 

