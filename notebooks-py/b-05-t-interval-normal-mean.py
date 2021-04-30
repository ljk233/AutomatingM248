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
# # Exact confidence intervals: normal mean
#
# date: 2021-04-16
#
# aim: Calculate a 100(1-a)% exact confidence interval for a
# normal mean
#
# reference: M248 Computer book B, Activity 21
#
# source: schoolgirls.csv
#
# description: Height (cm) and weight (kg) of 30 eleven-year-old
# schoolgirls from Bradford
#
# modules: `scipy`

# %% [markdown]
# ## Setup

# %%
from src import load
from scipy.stats import t, probplot
from math import sqrt
import seaborn as sns
import matplotlib.pyplot as plt

# %%
# import the data
schoolgirls = load.schoolgirls()

# %%
# assign column to local var
h = schoolgirls["Height"]

# %% [markdown]
# ## Visualise

# %%
h.plot(kind="box")
plt.show()

# %% [markdown]
# ## Calculate a 100(1-a)% exact confidence interval

# %% [markdown]
# ### Check assumption of normality

# %%
sns.set_theme()
f, ax = plt.subplots()
probplot(x=h,plot=ax)
plt.show()

# %% [markdown]
# The points lie roughly along a straight-line.
# This suggests a normal model is plausible for the heights of
# schoolgirls in Bradford.

# %% [markdown]
# ### Return the confidence interval

# %%
t.interval(
    alpha=0.9,
    df=h.size-1,
    loc=h.mean(),
    scale=h.std()/sqrt(h.size))
