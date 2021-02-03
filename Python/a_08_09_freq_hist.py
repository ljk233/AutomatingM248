
# =============================================================================
# References
# ==========
#
# - Computer activity 8 and Computer activity 9
# - Frequency histograms (HB.p5. U1.3.2. CA2.1.)
# - Plot a frequency histogram.
# =============================================================================

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# import the data
df = pd.read_csv("./data/membership.csv")

# preview data
df.head()

# =============================================================================
# Plot a frequency histogram
# =============================================================================

f, ax = plt.subplots()

sns.histplot(data=df,
             x="Percentage",
             edgecolor="none",  # remove the borders
             color="royalblue")

plt.show()

# =============================================================================
# Modify the binwidth.
# =============================================================================

f, ax = plt.subplots()

sns.histplot(data=df,
             x="Percentage",
             binwidth=1,        # set bins to width 1
             edgecolor="none",  # remove the borders
             color="royalblue")

plt.show()
