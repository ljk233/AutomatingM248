
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
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

pois = poisson(mu=3)

# calculate p(3)
pois.pmf(k=3)

# calculate F(3)
pois.cdf(x=3)

# Calculate P(X>1)
pois.sf(x=1)

# calculate E(X), V(X)
# redundant, as this is the parameter, but nevermind
pois.mean()
pois.var()

# =============================================================================
# Plot the p.m.f.
# =============================================================================

x = np.arange(pois.ppf(0.01), pois.ppf(0.99))  # generate sensible range for X

f, ax = plt.subplots()

sns.barplot(x=x,
            y=np.array(pois.pmf(x)),  # calaculate Pr(X)
            color="royalblue")

plt.show()
