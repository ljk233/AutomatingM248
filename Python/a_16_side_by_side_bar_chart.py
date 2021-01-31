
# =============================================================================
# References
# ==========
#
# - Computer activity 16
# - Side-by-side bar charts (HB.p5. U1.5.1. CA4.1.)
# - Plot a side-by-side bar chart of some data.
# =============================================================================

import pandas as pd
import plotly.express as px

# import the data
df = pd.read_csv("./data/tattoos.csv")

# preview the data
df.head()

# =============================================================================
# aggregate the data
# =============================================================================

score_count = df.groupby(["Depth", "Score"]).count()  # Count frequency of each Score
score_count.reset_index(inplace=True)  # reset the index, good practice
score_count.drop_duplicates(["Depth", "Score"], inplace=True)  # drop duplicate
score_count.rename(columns={"Size": 'Frequency'}, inplace=True)  # rename col
score_count.head()  # preview the dataframe

# =============================================================================
# Plot the side-by-side bar chart by declaring color and barmode.
# =============================================================================

fig = px.bar(score_count,
             x="Score",
             y="Frequency",
             color="Depth",
             barmode='group')
fig.show()
