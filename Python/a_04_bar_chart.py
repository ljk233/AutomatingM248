
# =============================================================================
# References
# ==========
#
# - Computer activity 4
# - Bar chart (HB.pp5; U1.3.1; CA1.2).
# - Plot a bar chart of raw data.
# =============================================================================

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# import the data
tattoos = pd.read_csv("./data/tattoos.csv")

# =============================================================================
# plot the bar chart using countplot
# =============================================================================

f, ax = plt.subplots()

sns.countplot(data=tattoos,
              x="Score",
              color="royalblue")

plt.show()
