
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
# Histogram of waiting times overlaid by a plot of M(lamba)
# Construct the model first
# =============================================================================

# scale = 1/lambda, where lamba = 1/mu
m = expon(loc=0, scale=coal["Interval"].mean())
X = np.linspace(m.ppf(0.01),
                m.ppf(0.99), 100)

model = pd.DataFrame()
model["X"] = X
model["f"] = model["X"].apply(m.pdf)

# add plots
f, ax = plt.subplots()

# add interval histogram
sns.histplot(data=coal,
             x="Interval",
             stat="density")

# add model pdf
sns.lineplot(data=model,
             x="X",
             y="f",
             color='red', lw=3, alpha=0.5, label='expon pdf')

plt.show()

# =============================================================================
# Rate of occurrence
# =============================================================================

# add event id
coal["Event"] = np.arange(start=1, stop=coal["Interval"].size+1)

# Add cumulative sum
coal["Days passed"] = coal["Interval"].cumsum()


coal.head()

# plot the time series
f, ax = plt.subplots()

# add interval histogram
sns.scatterplot(data=coal,
                x="Event",
                y="Days passed")
