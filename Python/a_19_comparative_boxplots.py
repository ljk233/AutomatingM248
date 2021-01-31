
# =============================================================================
# References
# ==========
#
# - Computer activity A.19
# - Comparative boxplots (HB.p5; U1.5.3; CA4.3)
# - Plot multiple boxplots as a comparative boxplot
# =============================================================================

import pandas as pd
import plotly.express as px

# import the data
df = pd.read_csv("./data/response-inhibition.csv")

# preview the DataFrame
df.head()

# check dtypes
df.dtypes

# =============================================================================
# Light data transformation to recast the categorical data
# =============================================================================

# Recast Group -> cat
df = df.astype({'Group': 'category'})

# recode Groups to Treatment, Control
df['Group'].replace({0: 'Control', 1: 'Treatment'}, inplace=True)

df.head()

# =============================================================================
# Output multiple horizontal boxplots
# =============================================================================

fig = px.box(df,
             x="Weight change",
             y="Group",
             color="Group")    # declare the categories
fig.show()

# =============================================================================
# Output multiple vertical boxplots, simply seap x for y
# =============================================================================

fig = px.box(df,
             x="Group",
             y="Weight change",
             color="Group")    # declare the categories
fig.show()
