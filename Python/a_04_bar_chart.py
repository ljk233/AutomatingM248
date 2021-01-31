
# =============================================================================
# References
# ==========
#
# - Computer activity 4
# - Bar chart (HB.pp5; U1.3.1; CA1.2).
# - Plot a bar chart of raw data.
# =============================================================================

import pandas as pd
import plotly.express as px

# import the data
tattoos = pd.read_csv("./data/tattoos.csv")

# =============================================================================
# aggregate the data
# =============================================================================

score_count = tattoos.groupby("Score").count()  # Count frequency of each Score
score_count.reset_index(inplace=True)  # reset the index, good practice
score_count.drop_duplicates("Score", inplace=True)  # drop duplicate
score_count.rename(columns={"Size": 'Frequency'}, inplace=True)  # rename col
score_count[["Score", "Frequency"]].head()  # preview the dataframe

# =============================================================================
# plot the bar chart
# =============================================================================

fig = px.bar(score_count,
             x="Score",
             y="Frequency")
fig.show()
