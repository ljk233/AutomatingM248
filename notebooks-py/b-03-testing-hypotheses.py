# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.11.1
#   kernelspec:
#     display_name: Python 3.8.2 64-bit
#     language: python
#     name: python38264bit42cc30f2071844968108c09d90e27cee
# ---

# %% [markdown]
# # Testing hypotheses
#
# **date** : 2021-04-17
#
# **aim:** Perform an hypothesis test
#
# **reference** : M248, computer book B, chapter 7
#
# **packages:** `statsmodels`, `scipy`

# %% [markdown]
# ## 1. Setup

# %%
# load the libraries
from setup import load
from statsmodels.stats.weightstats import ztest, zconfint
from statsmodels.stats.proportion import proportion_confint, proportions_ztest
from scipy.stats import probplot, ttest_1samp, ttest_rel
from math import sqrt
import seaborn as sns
import matplotlib.pyplot as plt

# %%
sns.set_theme()

# %% [markdown]
# ## 2. The $z$-test
#
# **aim** : Test the hypotheses $H_{0} : \mu = 47.1\%, \> H_{1} : \mu \neq 47.1\%$, where $\mu$ is the mean total pass rate for the driving practical test nationally across all UK test centres during the period April 2014 to March 2015.
#
# **reference** : activity 23
#
# **data** : practical-test.csv
#
# **description** : Pass rates for 316 UK driving practical test centres over the period April 2014 to March 2015.

# %% [markdown]
# ### 2.1 Import the data

# %%
# load data, assign column to local var
rt = load.practical_test()["Total"]

# %% [markdown]
# ### 2.2 Visualise the data

# %%
ax = sns.histplot(x=rt, edgecolor="none", color="cornflowerblue")
ax.set(xlabel="Percentage", ylabel="Frequency")
plt.show()

# %% [markdown]
# ### 2.3 Perform the $z$-test

# %%
# get the z-interval
zconfint(x1=rt)

# %% [markdown]
# Note that the `ztest()` returns `(test_statistic, p_value)`.

# %%
# perform the z-test
ztest(x1=rt, value=47.1)

# %% [markdown]
# Given $p <$ 0.01, there is strong evidence against the null hypothesis.
# The data suggests that the mean total pass rate from April 2013 to March 2014 was not equal to that from April 2012 to March 2013.
# Furthermore, with $Z > 0$, there is strong evidence to indicate that the mean total pass rate was greater from April 2013 to March 2014 compared to April 2012 to March 2013.

# %% [markdown]
# ## 3. The paired $t$-test
#
# **aims** : First, test the hypothesis $H_{0} : \mu_{D} = 0, \> \mu_{D} > 0$, where $\mu_{D}$ is the underlying population mean difference between the heights of paired plants. (See description.)
#
# Second, test the hypothesis $H_{0} : \mu_{X} = \mu_{S}, \> \mu_{X} > \mu_{S}$, where $\mu_{X}, \> \mu_{S}$ are the underlying population mean heights of the paired cross- and self-fertilised plants, respectivly. (See description.)
#
# **reference** : activity 25
#
# **data** : darwn.csv
#
# **description** : Heights of fifteen pairs of plants of the species *Zea mays*.
# Each plant had parents grown from the same seed, where one plant in each pair was the offspring of a cross-fertilisation, the other of a self-fertilisation.

# %% [markdown]
# ### 3.1 Import the data

# %%
# import the data
darwin = load.darwin()

# %%
# assign diff to local var
d = darwin["Cross"] - darwin["Self"]  # calculate the difference

# %% [markdown]
# ### 3.2 Visualise the data

# %% [markdown]
# #### 3.2.1 Visualise both data

# %%
ax = sns.boxplot(data=darwin.melt(), x="value", y="variable")
ax.set(xlabel="height (cm)", ylabel="")
plt.show()

# %% [markdown]
# #### 3.2.2 Visualise the difference

# %%
ax = sns.boxplot(x=d)
ax.set(xlabel="height (cm)", ylabel="difference in heights")
plt.show()

# %% [markdown]
# ### 3.3 Perform the $t$-tests

# %% [markdown]
# #### 3.3.1 Check assumption of normality

# %%
ax = plt.subplot()
probplot(x=d, plot=ax)
plt.show()

# %% [markdown]
# The points lie roughly along a straight-line.
# This suggests a normal model is plausible for the difference
# in heights between paired cross- and self-fertilised plants.

# %% [markdown]
# #### 3.3.2 Perform the $t$-test on the *difference*

# %% [markdown]
# Note that both `ttest_1samp()` returns `(test_statistic, p-value)`

# %%
ttest_1samp(a=d, popmean=0, alternative="greater")

# %% [markdown]
# Given $p \in$ (0.01, 0.05], there is moderate to strong evidence against the null hypothesis.
# We conclude that there is evidence to suggest that the mean difference in heights of the plants is greater than zero with cross-fertilised plants being taller on average than self-fertilised plants.

# %% [markdown]
# #### 3.3.3 Peform the $t$-test using *both data*
#
# Note that both `ttest_rel()` returns `(test_statistic, p-value)`

# %%
# perform the test
ttest_rel(a=darwin["Cross"], b=darwin["Self"], alternative="greater")

# %% [markdown]
# *(It is reassuring that this test gives the same result!)*
#
# Given $p \in$ (0.01, 0.05], there is moderate to strong evidence against the null hypothesis.
# The data indicates that there is moderate evidence in support of the claim that the mean height of the cross-fertilised plants is greater on average than self-fertilised plants.

# %% [markdown]
# ## 4. Testing a proportion
#
# **aim** : Test the hypothesis $H_{0} : p_{W} = 0.25, \> p_{W} \neq 0.25$, 
# where the $p_{W}$ is the proportion of young adults from 20 to 34 years-old living with their parents in Wales in 2014. (See description.)
#
# **reference** : activity 26
#
# **data** : N/A
#
# **description** : The Labour Force Survey (ONS, 2014) of 254 young people aged between 20 and 34 years living in Wales found that 68 were still living at home with their parents.
# Previous surveys had found the same proportion to be one-in-four young adults still lived with their parents.

# %% [markdown]
# ### 4.1 Perform the test of a proportion

# %%
# get the z-interval
proportion_confint(count=68, nobs=254)

# %% [markdown]
# Note that `proportion_ztest()` returns `(test_statistic, p-value)`.

# %%
# perform the hypothesis test
proportions_ztest(
    count=68,
    nobs=254,
    value=0.25,
    prop_var=0.25)

# %% [markdown]
# Given that $p >$ 0.1, there is little to no evidence against the null hypothesis.
