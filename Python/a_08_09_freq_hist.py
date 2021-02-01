
# =============================================================================
# References
# ==========
#
# - Computer activity 8 and Computer activity 9
# - Frequency histograms (HB.p5. U1.3.2. CA2.1.)
# - Plot a frequency histogram.
# =============================================================================

import pandas as pd
import plotly.express as px

# import the data
df = pd.read_csv("./data/membership.csv")

# preview data
df.head()

# =============================================================================
# Plot a frequency histogram
# =============================================================================

fig = px.histogram(df, x="Percentage")
fig.show()

# =============================================================================
# Modify the binwidth.
# =============================================================================

fig = px.histogram(df, x="Percentage")

# Check the min, max. Set the size to desired width
df["Percentage"].min()
df["Percentage"].max()
set_bins = dict(start=16.0, end=28.0, size=1)

fig.update_traces(xbins=set_bins)

fig.show()
