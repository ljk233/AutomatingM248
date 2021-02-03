
# =============================================================================
# References
# ==========
#
# - Computer activity A.17
# - Unit-area histograms (HB.p5. U1.5.2. CA4.2.)
# - Plot a unit-area histogram of some data.
# =============================================================================

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# import the data
df = pd.read_csv("./data/membership.csv")

# preview data
df.head()

# =============================================================================
# Plot a unit-area by declaring stat="density"
# =============================================================================

f, ax = plt.subplots()

sns.histplot(data=df,
             x="Percentage",
             binwidth=1,            # set bins to width 1
             edgecolor="none",    # remove the borders
             stat="density",
             color="royalblue")

plt.show()
