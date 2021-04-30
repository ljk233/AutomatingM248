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
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Large-sample approximate confidence intervals for proportions
#
# date: 2021-04-16
#
# aim: Calculate a 100(1-a)% approximate confidence interval for a
# proportion
#
# reference: M248 Computer book B, Activity 18
#
# data: accidents.csv
#
# description: Number of accidents suffered by each of 414 machinists
# over a period of time
#
# package: `statsmodels`

# %% [markdown]
# ## Setup

# %%
# import the packages
from __future__ import annotations
from setup import load
from statsmodels.stats.proportion import proportion_confint
import seaborn as sns
import matplotlib.pyplot as plt

# %%
# import data
accidents = load.accidents()

# %% [markdown]
# ## Visualise

# %%
sns.countplot(
    data=accidents,
    x="Accidents",
    color="cornflowerblue")
plt.show()

# %% [markdown]
# ## Calculate a 100(1-a)% confidence interval

# %%
# count number of entries where accidents != 0
x = accidents.query('Accidents != 0').count()[0]

# %%
# count the number of rows in totals
n = accidents["Accidents"].size

# %%
# return the confidence interval
proportion_confint(count=x, nobs=n, alpha=0.01)
