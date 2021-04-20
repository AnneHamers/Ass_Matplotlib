from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
from pandas.api.types import is_string_dtype
from pandas.api.types import is_numeric_dtype
import io

indicators = pd.read_csv("/content/drive/MyDrive/smoking-indicators.csv", delimiter=';', thousands=',')

# Drop borough id
indicators.drop('la', inplace=True, axis=1)

# Convert to usable arrays
# For chart 1
boroughs = indicators['Borough name']
smoking_2010_total = indicators['Smoking Status (2010): Total'].to_numpy()

#Chart 1: Smokers in 2010

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ax.barh(boroughs, smoking_2010_total, height=0.8)
ax.set_title('Number of smokers in Londen in 2010, per borough')
ax.set_xlabel('Number of smokers')
ax.set_ylabel('Borough')
ax.invert_yaxis()
ax.grid(True)
fig.set_size_inches(15, 10)
ticks = np.arange(0, 300000, 25000)
ax.set_xticks(ticks)
plt.show()

#Chart 2: Active smokers for 10 boroughs

# For chart 2
total = indicators[['Borough name','Smoking Status (2010): Total','Smoking Status (2011): Total','Smoking Status (2012): Total','Smoking Status (2013): Total']]
# Rename the columns
total.columns = ['boroughs', '2010','2011','2012','2013']
# Using all the boroughs makes for an illegible chart
total = total[0:10]

fig, ax = plt.subplots()
for index, row in total.iterrows():
  x = np.arange(2010, 2014)
  y = [row[1], row[2], row[3], row[4]]
  Label_name = str(row[0])
  plt.plot(x, y, label=Label_name)
fig.set_size_inches(15, 10)
ax.set_xlabel('Year')
ax.set_ylabel('Number of smokers')
ax.set_title('Number of smokers in London, per borough, for the years 2010 to 2013')
ax.grid(True)
ticksx = np.arange(2010, 2014, 1)
ax.set_xticks(ticksx)
ticksy = np.arange(120000, 300000, 10000)
ax.set_yticks(ticksy)
ax.legend(bbox_to_anchor=(1.0, 1.0))
plt.show()
