
"""----------------------------------------------------------------------------
References
==========

Computer activity A.15

Summarising grouped data
- Sample mean (HB.pp6; U1.4.1; CA3).
- Sample median (HB.pp6; U1.4.1; CA3).
- Sample quartiles (HB.pp6; U1.4.1; CA3).
- Sample IQR (HB.pp6; U1.4.1; CA3).
- Sample standard deviation (HB.pp6; U1.4.1; CA3).

Use Pandas to calculate numerical summaries of some data.
Output comparative boxplots of the data.

This differs to Computer Activity 14 (a_14.py) because here we wish to
group the data.
----------------------------------------------------------------------------"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# import the data
df = pd.read_csv("./data/response-inhibition.csv")

# preview the DataFrame
df.head()

"""----------------------------------------------------------------------------
There is some light data transformation to support the plotting of the
boxplot later in the exercise.
----------------------------------------------------------------------------"""

# check dtypes
df.dtypes

# Recast Group -> cat
df = df.astype({'Group': 'category'})

# recode Groups to Treatment, Control
df['Group'].replace({0: 'Control', 1: 'Treatment'}, inplace=True)

df.head()

"""----------------------------------------------------------------------------
Data is merged. Use groupby() to stratify the data
----------------------------------------------------------------------------"""

# Select Groups, Weight Change, and then Groupby
df_grouped = df[['Group', 'Weight change']].groupby("Group")

"""----------------------------------------------------------------------------
Output default descriptive table.
----------------------------------------------------------------------------"""

# output a simple table of summary measures
df_grouped.describe()

"""----------------------------------------------------------------------------
Return individual summary measures.
----------------------------------------------------------------------------"""

# sample mean
df_grouped.mean()

# sample median
df_grouped.median()

# sample quartiles
df_grouped.quantile(0.25)  # lower sample quartile

df_grouped.quantile(0.75)  # upper sample quartile

# Sample IQR
df_grouped.quantile(0.75) - df_grouped.quantile(0.25)

# sample standard deviation
df_grouped.std()

"""----------------------------------------------------------------------------
Output comparative boxplots of the data.
Note we return to the original DataFrame for this exercise.
----------------------------------------------------------------------------"""

sns.set_theme(style="white")        # set theme of sns
f, ax = plt.subplots()              # setup the figure, axis

sns.boxplot(data=df,
            x="Weight change",
            y="Group")

ax.set(xlabel="Weight change",
       title="Weight Change of Groups by Percentage")

plt.show()
