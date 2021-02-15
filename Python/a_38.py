
# =============================================================================
# References
# ==========
#
# - Computer activity A38
# - Confirming the Poisson process (HB.p10. U5.3.2. CA10).
# - Investigate the rate of occurrence and the waiting time between events
# =============================================================================

import pandas as pd
from scipy.stats import expon
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

coal = pd.read_csv("./data/coal.csv")

coal.head()

# =============================================================================
# Histogram of waiting times overlaid by a plot of M(lamba).
# Construct the model first
# =============================================================================

# scale = 1/lambda, where lamba = 1/mu
m = expon(loc=0, scale=coal["Interval"].mean())
x = np.linspace(m.ppf(0.01),
                m.ppf(0.99), 100)

# add plots
f, ax = plt.subplots()
sns.set_theme(style="darkgrid")

# add interval histogram
sns.histplot(data=coal,
             x="Interval",
             stat="density",
             color="royalblue")

# add model pdf
sns.lineplot(x=x,
             y=m.pdf(x),
             color='red', lw=3, alpha=0.5, label='Model')

ax.set(title="Waiting Time Between Events")

plt.show()

# =============================================================================
# Rate of occurrence
# =============================================================================

# add event id
coal["Event"] = np.arange(start=1, stop=coal["Interval"].size+1)

# Add cumulative sum
coal["Days passed"] = coal["Interval"].cumsum()

# plot the time series
f, ax = plt.subplots()
sns.set_theme(style="darkgrid")

# add interval histogram
sns.scatterplot(data=coal,
                x="Event",
                y="Days passed",
                color="royalblue")

ax.set(title="Rate of Occurrence")

plt.show()
