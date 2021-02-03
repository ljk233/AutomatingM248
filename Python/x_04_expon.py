
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
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

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

x = np.linspace(m.ppf(0.01), m.ppf(0.99), 100)  # generate sensible range for X

f, ax = plt.subplots()

sns.lineplot(x=x,
             y=np.array(m.pdf(x)),  # calaculate Pr(X)
             color="royalblue")

plt.show()
