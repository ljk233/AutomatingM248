
# =============================================================================
# References
# ==========
#
# - No corresponding activity
# - Binomial distributions
#   - About: HB.p8. U3.2.1;
#   - Mean and variance: U4.1.2. and U4.3.2
#
# Suppose that a discrete rv is distributed B(10, 0.5)
#
# - Calculate P(X=7)
# - Calculate F(4)
# - Calculate P(X>7)
# - Calculate E(X)
# - Calculate V(X)
# - Plot the p.m.f.
# =============================================================================

from scipy.stats import binom
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

b = binom(n=10, p=0.5)

# calculate p(7)
b.pmf(k=7)

# calculate F(4)
b.cdf(x=4)

# Calculate P(X>7)
b.sf(x=7)

# calculate E(X), V(X)
b.mean()
b.var()

# =============================================================================
# Plot the p.m.f.
# =============================================================================

x = np.arange(b.ppf(0.01), b.ppf(0.99))  # generate sensible range for X

f, ax = plt.subplots()

sns.barplot(x=x,
            y=np.array(b.pmf(x)),  # calaculate Pr(X)
            color="royalblue")

plt.show()
