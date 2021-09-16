#%%
import pandas as pd
world = pd.read_csv("https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv")
# %%
world_subset = world[['Mortality rate, infant (per 1,000 live births)', 'GDP per capita (constant 2010 US$)', 'Country Name']]
# %%
import matplotlib.pyplot as plt
world_subset[['Mortality rate, infant (per 1,000 live births)', 'GDP per capita (constant 2010 US$)']].plot(kind='scatter', x = 'GDP per capita (constant 2010 US$)', y= 'Mortality rate, infant (per 1,000 live births)')
# %%
