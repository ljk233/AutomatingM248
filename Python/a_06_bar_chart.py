
"""----------------------------------------------------------------------------
References
==========

Computer actitity 6

- Bar chart (HB.pp5; U1.3.1; CA1.2).

Plot a bar chart of aggregated data.
----------------------------------------------------------------------------"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# import the data
df = pd.read_csv("./data/workforce.csv")

# preview data
df.head()

"""----------------------------------------------------------------------------
Plot a default barplot
----------------------------------------------------------------------------"""

# plot the bar chart
sns.set_theme(style="darkgrid")         # set theme of sns
f, ax = plt.subplots()                  # setup the figure, axis

ax = sns.barplot(data=df,               # sets the dataframe
                 x="Occupation type",   # set the x-axis
                 y="Total",             # set the y-axis
                 color="royalblue")     # set the colour scheme

# set y-axis and title
ax.set(xlabel="",                       # suppress the x label
       ylabel="Frequency",
       title="Total number of workers by occupation type")

plt.xticks(rotation=70)                 # rotate the x axis labels
plt.show()

"""----------------------------------------------------------------------------
Change the order of the bars in the plot
----------------------------------------------------------------------------"""

# plot the bar chart
sns.set_theme(style="darkgrid")         # set theme of sns
f, ax = plt.subplots()                  # setup the figure, axis

# order bar chart in descending order by total
an_order = df.sort_values(by="Total", ascending=False)["Occupation type"]

ax = sns.barplot(data=df,               # sets the dataframe
                 x="Occupation type",   # set the x-axis
                 y="Total",             # set the y-axis
                 color="royalblue",     # set the colour scheme
                 order=an_order)

# set y-axis and title
ax.set(xlabel="",                       # suppress the x label
       ylabel="Frequency",
       title="Total number of workers by occupation type")

plt.xticks(rotation=70)                 # rotate the x axis labels
plt.show()
