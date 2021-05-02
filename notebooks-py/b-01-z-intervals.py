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
# # Large-sample confidence intervals
#
# **date** : 2021-04-16
#
# **aim** : Calculate 100(1-a)% large-sample confidence intervals
#
# **reference** : M248, computer book B, chapter 5
#
# **packages** : `statsmodels`, `scipy`
#
# **contents** :
#
# 1. Setup the notebook
# 2. Confidence interval for a population mean
# 3. Confidence interval for a proportion
# 4. Confidence interval for the difference between two proportions

# %% [markdown]
# ## 1. Setup the notebook

# %%
from __future__ import annotations
from src import load
from statsmodels.stats.weightstats import zconfint
from statsmodels.stats.proportion import (
    proportion_confint, confint_proportions_2indep)
from scipy.stats import norm
from math import sqrt
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# %%
# set seaborn to default theme
sns.set_theme()

# %% [markdown]
# ## 2. Confidence interval for a population mean
#
# **aim** : Calculcate a 95% $z$-interval for the mean strength of
# glass fibres.
#
# **reference** : activity 15
#
# **data** : glass-fibres.csv
#
# **description** : Strengths of glass-fibres of length 1.5cm
#
# **note** : this exercise is done twice, first using the data
# directly, second using the values

# %% [markdown]
# ### 2.1 Import the data

# %%
# import the data and assign local var
fibres = load.glass_fibres()

# %% [markdown]
# ### 2.2 Visualise the data

# %%
sns.histplot(
    data=fibres,
    x="Strength",
    binwidth=0.2,
    color="cornflowerblue")
plt.show()

# %% [markdown]
# ### 2.3 Calculate a 100(1-a)% confidence interval for a population mean
#
# #### 2.3.1 Using the data
#
# Note that `param=a` should be the $\alpha$ in $100(1-\alpha)\%$

# %%
zconfint(x1=fibres["Strength"], alpha=0.05)

# %% [markdown]
# #### 2.3.2 Using the values
#
# If instead we have the values for the mean, standard deviation, and
# size (instead of some data), we could use `scipy.stats.norm` to
# calculate the confidence interval.

# %%
# get the parameters
{"mean": fibres["Strength"].mean(),
 "std": fibres["Strength"].std(),
 "size": fibres["Strength"].size}

# %%
# return the confidence interval
norm(loc=1.51, scale=0.324/sqrt(63)).interval(0.95)

# %% [markdown]
# ## 3. Confidence intervals for a proportion
#
# **aim** : Calculate a 99% $z$-interval for the proportion of workers
# who suffered at least one accident at work.
#
# **reference** : activity 18
#
# **data** : accidents.csv
#
# **description** : Number of accidents suffered by each of 414 machinists
# over a period of time

# %% [markdown]
# ### 3.1 Import the data

# %%
# import data
accidents = load.accidents()

# %% [markdown]
# ### 3.2 Visualise the data

# %%
sns.countplot(
    data=accidents,
    x="Accidents",
    color="cornflowerblue")
plt.show()

# %% [markdown]
# ### 3.3 Calculate a 100(1-a)% confidence interval for a proportion

# %%
# count number of entries where accidents != 0
x = accidents.query('Accidents != 0').count()[0]

# %%
# count the number of rows in totals
n = accidents["Accidents"].size

# %%
# return the confidence interval
proportion_confint(count=x, nobs=n, alpha=0.01)

# %% [markdown]
# ## 4. Confidence interval for the difference between two proportions
#
# **aim** : Calculate a 95% $z$-interval for the difference between the
# proportion infected amog sewerage workers *with* and *without* children
#
# **reference**: activity 20
#
# **data** : sewer.csv
#
# **description** : Occupational risk to sewerage workers of hepatitis
# A infection though contact with raw sewage.
#
# Relevant fields for this example:
#
# - Immunity=`(0=no immunity, 1=immunity)`
# - Children=`(0=no children, 2=children)`

# %% [markdown]
# ### 4.1 Import the data

# %%
# import the data
sewer = load.sewer()

# %% [markdown]
# ### 4.2 Visualise the data

# %%
# group the data and count
gsewer = sewer.groupby(["Immunity", "Children"]).count()
gsewer.reset_index(inplace=True)
gsewer.rename(columns={"Age": "Freq"}, inplace=True)

# %%
# plot the data
ax = sns.barplot(
    data=gsewer,
    x="Immunity",
    y="Freq",
    hue="Children")
plt.show()

# %% [markdown]
# ### 4.3 Calculate a 100(1-a)% confidence interval for the difference
# between two proportions

# %%
# construct contingency table
pd.crosstab(
    index=sewer["Children"],
    columns=sewer["Immunity"],
    margins=True)

# %% [markdown]
# Note, default actual argument for formal agument `method=newcomb`
# does not return the result expected in M248.

# %%
confint_proportions_2indep(
    count1=68,  # has children, has immunity
    nobs1=158,  # has children
    count2=11,  # no children, has immunity
    nobs2=70,   # no children
    method="wald")
