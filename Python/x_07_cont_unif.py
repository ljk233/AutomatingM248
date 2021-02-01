
# =============================================================================
# References
# ==========
#
# - No corresponding activity
# - Continuous uniform distributions
#    - About: HB.p8. U3.5.2
#    - Mean and variance: HB.p7. U2.2.1.
#    - Standard uniform: U3.5.3;
#
# Suppose that a discrete rv is distributed U(0, 1)
#
# - Calculate F(0.75)
# - Calculate P(X>0.175)
# - Calculate E(X)
# - Calculate V(X)
# - Plot the p.d.f.
# =============================================================================

from scipy.stats import uniform
import pandas as pd
import numpy as np
import plotly.express as px

u = uniform(0, 1)

# calculate F(0.75)
u.cdf(x=0.75)

# calculate P(X>=0.175)
u.sf(x=0.175)

# calculate mean
u.mean()

# calculate var
u.var()

# =============================================================================
# Plot the p.d.f.
# =============================================================================

pdf = pd.DataFrame()
pdf["x"] = np.linspace(start=0, stop=1, num=1000)
pdf["f(x)"] = pdf["x"].apply(u.pdf)

fig = px.line(pdf,
              x="x",
              y="f(x)")

fig.show()
