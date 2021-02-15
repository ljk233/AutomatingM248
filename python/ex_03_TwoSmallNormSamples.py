
# =============================================================================
# About
# =====
# 1. Generate two samples: one for Cardiff, one Narnia
# 2. Plot the histograms
# 3. Normal probability plots
# 4. Estimate the parameters
# 5. Confidence interval for the difference
# 6. Transform to cm
# 6. Calculate probabilities using females
# =============================================================================

from scipy.stats import probplot
import seaborn as sns
import matplotlib.pyplot as plt
from util.SampleTest import TwoSmallNormalSamples

# =============================================================================
# 1. Generate samples from a normal distribution
# =============================================================================

# create the test object
test = TwoSmallNormalSamples()

# generate the samples
test.generate_samples(mean=15, var=2, n1=17, n2=9)

# =============================================================================
# 2. Plot the histogram
# =============================================================================

f, (ax1, ax2) = plt.subplots(1, 2)
sns.set_theme(style="darkgrid")

sns.histplot(x=test.has_s1(),
             edgecolor="none",  # remove the borders
             color="royalblue",
             ax=ax1)

sns.histplot(x=test.has_s2(),
             edgecolor="none",  # remove the borders
             color="orange",
             ax=ax2)

"""
ax.set(title="Frequency Histogram of Sample",
       xlabel="Tail Fin Width (Tinsotune)",
       ylabel="Frequency")
"""

f.tight_layout(pad=2.0)

plt.show()

# =============================================================================
# 3. Normal probability plots
# =============================================================================

f, (ax1, ax2) = plt.subplots(1, 2)
sns.set_theme(style="darkgrid")

res1 = probplot(test.has_s2(), plot=ax1)

res2 = probplot(test.has_s2(), plot=ax2)

f.tight_layout(pad=2.0)

plt.show()

# =============================================================================
# 4. Estimate the parameters
# =============================================================================

# mean, var of sample 1
test.has_s1_mean()
test.has_s1_var()

# mean, var of sample 2
test.has_s2_mean()
test.has_s2_var()

# =============================================================================
# 5. Check for common variance
# =============================================================================

test.do_samples_have_common_variance()

# =============================================================================
# 5. Confidence interval for difference
# =============================================================================

test.has_interval(0.95)

# =============================================================================
# 6. view the combined data
# =============================================================================

f, ax = plt.subplots()
sns.set_theme(style="darkgrid")

sns.histplot(x=test.has_s_comb(),
             edgecolor="none",  # remove the borders
             color="royalblue")

"""
ax.set(title="Frequency Histogram of Sample",
       xlabel="Tail Fin Width (Tinsotune)",
       ylabel="Frequency")
"""

f.tight_layout(pad=2.0)

plt.show()
