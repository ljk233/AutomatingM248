
"""----------------------------------------------------------------------------
References
==========

Computer activity 16

- Side-by-side bar chart

Plot a side-by-side bar chart of some data.
----------------------------------------------------------------------------"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# import the data
df = pd.read_csv("./data/tattoos.csv")

# preview the data
df.head()

"""----------------------------------------------------------------------------
Split the data into subcategories by setting the "hue" parameter.
----------------------------------------------------------------------------"""

sns.set_theme(style="whitegrid")        # set theme of sns
f, ax = plt.subplots()                  # setup the figure, axis

ax = sns.countplot(data=df,         # sets the dataframe
                   x="Score",       # set the x-axis
                   hue="Depth")     # separate the subcategories

# set y-axis and title
ax.set(ylabel="Frequency",
       title="Frequency of score by depth")

# move the legend outside the axes
plt.legend(bbox_to_anchor=(1, 1))
# display the plot
plt.show()
