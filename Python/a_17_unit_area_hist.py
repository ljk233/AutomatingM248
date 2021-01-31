
"""----------------------------------------------------------------------------
References
==========

Computer activity 17

- Unit-area histogram

Plot a unit-area histogram
----------------------------------------------------------------------------"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# import the data
df = pd.read_csv("./data/membership.csv")

# preview data
df.head()

"""----------------------------------------------------------------------------
Plot a unit-area histogram by specifying the stat='density' parameter.
----------------------------------------------------------------------------"""

# plot the bar chart
sns.set_theme(style="white")            # set theme of sns
f, ax = plt.subplots()                  # setup the figure, axis

ax = sns.histplot(data=df,              # sets the dataframe
                  x="Percentage",       # set the x-axis
                  stat="density",       # plot unit-area hist
                  binwidth=1,           # set bin width
                  color="royalblue")    # set the colour scheme

# set y-axis and title
ax.set(xlabel="Percentage",
       ylabel="Density",
       title="Unit-area histogram of percentage")

plt.show()
