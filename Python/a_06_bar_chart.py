
# =============================================================================
# References
# ==========
#
# - Computer actitity 6
# - Plot a bar chart of aggregated data.
# =============================================================================

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# import the data
df = pd.read_csv("./data/workforce.csv")

# preview data
df.head()

# =============================================================================
# Plot a default barplot
# =============================================================================

f, ax = plt.subplots()
sns.set_theme(style="darkgrid")

sns.barplot(data=df,
            x="Occupation type",
            y="Total",
            color="royalblue")

ax.set(title="Total workforce by Occupation type",
       xlabel="",   # Suppress x-axis label
       ylabel="Frequency (millions)")

plt.xticks(rotation=70)
plt.tight_layout()
plt.show()

# =============================================================================
# Change the order of the bars by defining the sort order as a var
# =============================================================================

# order the DataFrame in descending order by total
ordered_df = df.sort_values("Total", ascending=False)

f, ax = plt.subplots()

sns.barplot(data=ordered_df,
            x="Occupation type",
            y="Total",
            color="royalblue")

ax.set(title="Total workforce by Occupation type",
       xlabel="",   # Suppress x-axis label
       ylabel="Frequency (millions)")

plt.xticks(rotation=70)
plt.tight_layout()
plt.show()
