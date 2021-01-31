
# =============================================================================
# References
# ==========
#
# - Computer activity A.17
# - Unit-area histograms (HB.p5. U1.5.2. CA4.2.)
# - Plot a unit-area histogram of some data.
# =============================================================================

import pandas as pd
import plotly.express as px

# import the data
df = pd.read_csv("./data/membership.csv")

# preview data
df.head()

# =============================================================================
# Plot a unit-area by declaring the histnorm= parameter
# =============================================================================

fig = px.histogram(df, x="Percentage", histnorm='probability density')

# Check the min, max. Set the size to desired width
df["Percentage"].min()
df["Percentage"].max()
set_bins = dict(start=16.0, end=28.0, size=1)

fig.update_traces(xbins=set_bins)

fig.show()
