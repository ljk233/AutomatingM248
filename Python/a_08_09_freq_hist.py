
"""----------------------------------------------------------------------------
References
==========

Computer activity 8
Computer activity 9

- Frequency histogram (HB.pp5; U1.3.2; CA2.1).

Plot a frequency histogram
----------------------------------------------------------------------------"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# import the data
df = pd.read_csv("./data/membership.csv")

# preview data
df.head()

"""----------------------------------------------------------------------------
Plot a frequency histogram
----------------------------------------------------------------------------"""

# plot the bar chart
sns.set_theme(style="white")         # set theme of sns
f, ax = plt.subplots()                  # setup the figure, axis

ax = sns.histplot(data=df,              # sets the dataframe
                  x="Percentage",       # set the x-axis
                  color="royalblue")    # set the colour scheme

# set y-axis and title
ax.set(xlabel="Percentage",
       ylabel="Frequency",
       title="Frequency histogram of percentage")

plt.show()

"""----------------------------------------------------------------------------
Modify the binwidth.
----------------------------------------------------------------------------"""

# plot the bar chart
sns.set_theme(style="white")            # set theme of sns
f, ax = plt.subplots()                  # setup the figure, axis

ax = sns.histplot(data=df,              # sets the dataframe
                  x="Percentage",       # set the x-axis
                  binwidth=1,           # set bin width to 1
                  color="royalblue")    # set the colour scheme

# set y-axis and title
ax.set(xlabel="Percentage",
       ylabel="Frequency",
       title="Frequency histogram of percentage")

plt.show()
