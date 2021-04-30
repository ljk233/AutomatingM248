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
# # Large-sample confidence intervals: population mean
#
# date: 2021-04-16
#
# aim: Calculate a 100(1-a)% approximate confidence interval
# for a population mean
#
# reference: M248 Computer book B, Activity 15
#
# data: glass-fibres.csv
#
# description: Strengths of glass-fibres of length 1.5cm
#
# module: `statsmodels`

# %% [markdown]
# ## Setup

# %%
# import the packages
from __future__ import annotations
from src import load
from statsmodels.stats.weightstats import zconfint
import seaborn as sns
import matplotlib.pyplot as plt

# %%
# import the data and assign local var
fibres = load.glass_fibres()

# %% [markdown]
# ## Visualise

# %%
sns.histplot(
    data=fibres,
    x="Strength",
    binwidth=0.2,
    color="cornflowerblue")
plt.show()

# %% [markdown]
# ## Calculate a 100(1-a)% confidence interval
#
# Note that param=`a` should be the alpha in 100(1-alpha)%

# %%
zconfint(x1=fibres["Strength"], alpha=0.1)
