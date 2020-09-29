import pandas as pd
WDI = pd.read_csv('https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv')
WDI = WDI[['Mortality rate, infant (per 1,000 live births)','GDP per capita (constant 2010 US$)','Country Name']]
WDI.head()
from plotnine import *
(ggplot(WDI, aes(x='Mortality rate, infant (per 1,000 live births)',y='GDP per capita (constant 2010 US$)')) + geom_point())

