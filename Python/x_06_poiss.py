
# =============================================================================
# References
# ==========
#
# - No corresponding activity
# - Poisson distributions
#   - About: HB.p8. U3.4;
#   - Mean and variance: U4.1.2. and U4.3.2.
#
# Suppose that a discrete rv is distributed Poisson(3)
#
# - Calculate P(X=3)
# - Calculate F(3)
# - Calculate P(X>1)
# - Calculate E(X)
# - Calculate V(X)
# - Plot the p.m.f.
# =============================================================================

from scipy.stats import poisson
import pandas as pd
import numpy as np
import plotly.express as px

p = poisson(mu=3)

# calculate p(3)
p.pmf(k=3)

# calculate F(3)
p.cdf(x=3)

# Calculate P(X>1)
p.sf(x=1)

# calculate E(X), V(X)
# redundant, as this is the parameter, but nevermind
p.mean()
p.var()

# =============================================================================
# Plot the p.m.f.
# =============================================================================

pmf = pd.DataFrame()
pmf["X"] = np.arange(0, 11)
pmf["Pr"] = pmf["X"].apply(p.pmf)

fig = px.bar(pmf,
             x="X",
             y="Pr")
fig.show()
