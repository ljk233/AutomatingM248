
"""----------------------------------------------------------------------------
References
==========

Computer activity 11
Computer activity 12

- Boxplots (HB.pp5; U1.3.3; CA2.2).

Plot a boxplot.
----------------------------------------------------------------------------"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# import the data
df = pd.read_csv("./data/membership.csv")

# preview data
df.head()

"""----------------------------------------------------------------------------
Plot a horizontal boxplot
----------------------------------------------------------------------------"""

# plot the bar chart
sns.set_theme(style="darkgrid")     # set theme of sns
f, ax = plt.subplots()              # setup the figure, axis

ax = sns.boxplot(data=df,           # set the data
                 x='Percentage')    # plot horizontally by setting x

# set y-axis and title
ax.set(xlabel="Percentage",
       ylabel="",
       title="Boxplot of Percentage")

plt.show()

"""----------------------------------------------------------------------------
Plot a vertical boxplot
----------------------------------------------------------------------------"""

# plot the bar chart
sns.set_theme(style="darkgrid")     # set theme of sns
f, ax = plt.subplots()              # setup the figure, axis

ax = sns.boxplot(data=df,           # set the data
                 y='Percentage')    # plot horizontally by setting y

# set y-axis and title
ax.set(ylabel="Percentage",
       xlabel="",
       title="Boxplot of Percentage")

plt.show()
