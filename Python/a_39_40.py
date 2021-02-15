
# =============================================================================
# References
# ==========
#
# - Computer activities A39 and A40
# - Confirming the Poisson process (HB.p10. U5.3.2. CA10).
# - Investigate the rate of occurrence and does the distribution look
#   like a Poisson pmf?
# =============================================================================

import pandas as pd
from scipy.stats import poisson
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

review = pd.read_csv("./data/review-requests.csv")

review.head()

# =============================================================================
# Investigate the rate of occurrence.
# =============================================================================

review["Total number of requests"] = review["Requests"].cumsum()
review["Week"] = np.arange(start=1, stop=review["Requests"].size+1)

# plot the time series
f, ax = plt.subplots()

# add interval histogram
sns.scatterplot(data=review,
                x="Week",
                y="Total number of requests")

ax.set(title="Rate of Occurrences")

plt.show()

# =============================================================================
# Investigate the shape of the pmf
# =============================================================================

f, ax = plt.subplots()

# add interval histogram
sns.countplot(data=review,
              x="Requests",
              color="royalblue")

# calculate mu
mu = review["Requests"].mean()

# add the Poisson model
x = np.arange(poisson.ppf(0.01, mu),
              poisson.ppf(0.99, mu))
ax.plot(x, poisson.pmf(x, mu) * review["Requests"].size+1,
        'bo', ms=8, label='poisson model')
ax.vlines(x, 0, poisson.pmf(x, mu) * review["Requests"].size+1,
          colors='r', lw=3, alpha=0.5)

ax.set(title="Frequency of the Number of Events",
       xlabel="Requests per week",
       ylabel="Frequency")

plt.show()
