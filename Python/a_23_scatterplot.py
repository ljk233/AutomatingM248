
"""----------------------------------------------------------------------------
References
==========

Computer activity A.23

Scatterplots

Plot a scatterplot of some linked data.
----------------------------------------------------------------------------"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# import the data
df = pd.read_csv("./data/distance.csv")

# preview the DataFrame
df.head()

# check dtypes
df.dtypes

"""----------------------------------------------------------------------------
Output a scatterplot of Road distance vs Map distance.
----------------------------------------------------------------------------"""

sns.set_theme(style="darkgrid")     # set theme of sns
f, ax = plt.subplots()              # setup the figure, axis

sns.scatterplot(data=df,    # data
                x="Map",    # x-axis
                y="Road")   # y-axis

ax.set(xlabel="Distance by map",
       ylabel="Distance by road",
       title="Road distance against map distance")

plt.show()
