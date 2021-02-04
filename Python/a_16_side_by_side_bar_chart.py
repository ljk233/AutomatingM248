
# =============================================================================
# References
# ==========
#
# - Computer activity 16
# - Side-by-side bar charts (HB.p5. U1.5.1. CA4.1.)
# - Plot a side-by-side bar chart of some data.
# =============================================================================

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# import the data
df = pd.read_csv("./data/tattoos.csv")

# preview the data
df.head()

# =============================================================================
# Plot the side-by-side bar chart by declaring hue
# =============================================================================

f, ax = plt.subplots()
sns.set_theme(style="darkgrid")

sns.countplot(data=df,
              x="Score",
              hue="Depth")                  # set hue= to grouping

ax.set(title="Frequency of Score by Depth",
       xlabel="Score",
       ylabel="Frequency")

plt.legend(bbox_to_anchor=(1.05, 1))    # move legend

plt.show()
