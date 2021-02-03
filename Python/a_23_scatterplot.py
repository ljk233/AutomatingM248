
# =============================================================================
# References
# ==========
#
# - Computer activity A.23
# - Scatterplots (HB.p6; U1.5.4; CA4.4).
# - Plot a scatterplot of linked data
# =============================================================================

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# import the data
df = pd.read_csv("./data/distance.csv")

# preview the DataFrame
df.head()

# =============================================================================
# Plot the scatterplot
# =============================================================================

f, ax = plt.subplots()

sns.scatterplot(data=df,
                x="Road",
                y="Map")

plt.show()
