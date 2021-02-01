
# =============================================================================
# References
# ==========
#
# - Computer actitity 6
# - Bar charts (HB.p5. U1.3.1. CA1.2.)
# - Plot a bar chart of aggregated data.
#
# Note same can be done sns.countplot, plus without the need to
# aggregate the data first.
# =============================================================================

import pandas as pd
import plotly.express as px

# import the data
df = pd.read_csv("./data/workforce.csv")

# preview data
df.head()

# =============================================================================
# Plot a default barplot
# =============================================================================

fig = px.bar(df,
             x="Occupation type",
             y="Total")
fig.show()

# =============================================================================
# Change the order of the bars
# =============================================================================

# order bar chart in descending order by total
ordered_df = df.sort_values("Total", ascending=False)

fig = px.bar(ordered_df,
             x="Occupation type",
             y="Total")
fig.show()
