
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
import plotly.express as px

# import the data
df = pd.read_csv("./data/tattoos.csv")

# preview the DataFrame
df.head()

# =============================================================================
# Seaborn: Plot the bar chart using countplot
# =============================================================================

f, ax = plt.subplots()

sns.countplot(data=df,              # set the data
              x="Score",            # set the x-axis
              color="royalblue")    # set the colour

ax.set(title="Frequency of Score",  # set the title
       xlabel="Score",              # set x-label
       ylabel="Frequency")          # set y-label

plt.show()

# =============================================================================
# Plotly.express: We first need to aggregate the data.
# =============================================================================

# add a count column
df["Count"] = 0

# aggregate the DataFrame
df_count = df.groupby(["Score"]).agg("count")
df_count.reset_index(inplace=True)              # reset the index

f = px.bar(data_frame=df_count,                 # the DataFrame
           x="Score",                           # x-axis
           y="Count",                           # y-axis
           title="Frequency of Score",          # set the title
           labels={"Count": "Frequency"})       # relabel the y-axis

f.show()
