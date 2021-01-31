
"""----------------------------------------------------------------------------
References
==========

Computer activity 4

- Bar chart (HB.pp5; U1.3.1; CA1.2).

Plot a bar chart of raw data.
----------------------------------------------------------------------------"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# import the data
tattoos = pd.read_csv("./data/tattoos.csv")

# plot the bar chart
sns.set_theme(style="whitegrid")        # set theme of sns
f, ax = plt.subplots()                  # setup the figure, axis

ax = sns.countplot(data=tattoos,        # sets the dataframe
                   x="Score",           # set the x-axis
                   color="royalblue")   # set the colour scheme

# set y-axis and title
ax.set(ylabel="Frequency",
       title="Frequency of Score")

# display the plot
plt.show()
