
# =============================================================================
# References
# ==========
#
# - No corresponding activity
# - Discrete uniform distributions
#   - About: HB.p8. U3.4;
#   - Mean and variance: U4.1.2. and U4.3.2.
#
# Suppose that a discrete rv is distributed uniformly with m=1, n=6
#
# - Calculate P(X=3)
# - Calculate F(4)
# - Calculate P(X>1)
# - Calculate E(X)
# - Calculate V(X)
# - Plot the p.m.f.
# =============================================================================

from scipy.stats import randint
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# declare high to n+1
u = randint(low=1, high=7)

# calculate p(3)
u.pmf(k=3)

# calculate F(3)
u.cdf(x=4)

# Calculate P(X>1)
u.sf(x=1)

# calculate E(X), V(X)
u.mean()
u.var()

# =============================================================================
# Plot the p.m.f.
# =============================================================================

x = np.arange(u.ppf(0.01), u.ppf(0.99))  # generate sensible range for X

f, ax = plt.subplots()

sns.barplot(x=x,
            y=np.array(u.pmf(x)),  # calaculate Pr(X)
            color="royalblue")

plt.show()
