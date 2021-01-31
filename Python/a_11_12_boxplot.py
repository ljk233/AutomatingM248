
# =============================================================================
# References
# ==========
#
# - Computer activity 11 and Computer activity 12
# - Boxplots (HB.p5. U1.3.3. CA2.2.)
# - Plot a boxplot.
# =============================================================================

import pandas as pd
import plotly.express as px

# import the data
df = pd.read_csv("./data/membership.csv")

# preview data
df.head()

# =============================================================================
# Plot a horizontal boxplot
# =============================================================================

fig = px.box(df, x="Percentage")
fig.show()

# =============================================================================
# Plot a vertical boxplot
# =============================================================================

fig = px.box(df, y="Percentage")
fig.show()
