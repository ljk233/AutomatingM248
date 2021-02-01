
# =============================================================================
# References
# ==========
#
# - No corresponding activity
# - Geometric distributions
#   - About: HB.p8. U3.3.1;
#   - Mean and variance: U4.1.2. and U4.3.2
#
# Suppose that a discrete rv is distributed G(0.5)
#
# - Calculate P(X=3)
# - Calculate F(3)
# - Calculate P(X>4)
# - Calculate E(X)
# - Calculate V(X)
# - Plot the p.m.f.
# =============================================================================

from scipy.stats import geom
import pandas as pd
import numpy as np
import plotly.express as px

g = geom(p=0.5)

# calculate p(7)
g.pmf(k=3)

# calculate F(4)
g.cdf(x=3)

# Calculate P(X>7)
g.sf(x=4)

# calculate E(X), V(X)
g.mean()
g.var()

# =============================================================================
# Plot the p.m.f.
# =============================================================================

pmf = pd.DataFrame()
pmf["X"] = np.arange(0, 11)
pmf["Pr"] = pmf["X"].apply(g.pmf)

fig = px.bar(pmf,
             x="X",
             y="Pr")
fig.show()
