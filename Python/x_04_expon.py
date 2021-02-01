
# =============================================================================
# References
# ==========
#
# - No corresponding activity
# - Exponential distributions
#   - About: HB.p10. U5.2.1
#
# Suppose that a cts rv is distributed M(2)
#
# - Calculate F(0.5)
# - Calculate P(X>=1)
# - Calculate mean
# - Calculate var
# - Plot the p.d.f.
# =============================================================================

from scipy.stats import expon
import pandas as pd
import numpy as np
import plotly.express as px

lm = 2

# note, scale=1/mean
m = expon(loc=0, scale=1/lm)

# calculate F(0.5)
m.cdf(x=0.5)

# calculate P(X>=1)
m.sf(x=1)

# calculate mean
m.mean()

# calculate var
m.var()

# =============================================================================
# Plot the p.d.f.
# =============================================================================

pdf = pd.DataFrame()
pdf["x"] = np.linspace(start=0, stop=2, num=1000)
pdf["f(x)"] = pdf["x"].apply(m.pdf)

fig = px.line(pdf,
              x="x",
              y="f(x)")

fig.show()
