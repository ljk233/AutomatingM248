
"""----------------------------------------------------------------------------
References
==========

Computer activity A.19

Comparative boxplots

Plot multiple boxplots on the same axes.
----------------------------------------------------------------------------"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# import the data
df = pd.read_csv("./data/response-inhibition.csv")

# preview the DataFrame
df.head()

# check dtypes
df.dtypes

"""----------------------------------------------------------------------------
Some light data transformation to support the plotting of the Comparative
boxplots
----------------------------------------------------------------------------"""

# Recast Group -> cat
df = df.astype({'Group': 'category'})

# recode Groups to Treatment, Control
df['Group'].replace({0: 'Control', 1: 'Treatment'}, inplace=True)

df.head()

"""----------------------------------------------------------------------------
Output a boxplot of the data.
----------------------------------------------------------------------------"""

sns.set_theme(style="white")        # set theme of sns
f, ax = plt.subplots()              # setup the figure, axis

sns.boxplot(data=df,
            x="Weight change",
            y="Group")

ax.set(xlabel="Weight change",
       title="Weight Change by Percentage")

plt.show()

"""----------------------------------------------------------------------------
Output a vertical boxplot of the same data.
----------------------------------------------------------------------------"""

sns.set_theme(style="white")        # set theme of sns
f, ax = plt.subplots()              # setup the figure, axis

sns.boxplot(data=df,
            x="Group",
            y="Weight change")

ax.set(xlabel="Weight change",
       title="Weight Change by Percentage")

plt.show()
