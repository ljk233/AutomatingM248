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
# # Plot a normal probability plot
#
# date: 2021-04-10
#
# aim: Plot a normal probability plot of some data
#
# reference: M248 Computer book B, Activity 8
#
# data: plasma.csv
#
# description: Level of blood pasma nicotine levels of 55 smokers
#
# module: `scipy.stats.probplot`

# %% [markdown]
# ## Setup

# %%
# import packages
from __future__ import annotations
from src import load
from scipy.stats import probplot
import seaborn as sns
import matplotlib.pyplot as plt

# %%
# load data
plasma = load.plasma()

# %% [markdown]
# ## Describe

# %%
# inspect the data
plasma.head()

# %%
# summarise the data
plasma.describe()

# %%
# plot the data
sns.histplot(data=plasma, x="Level")
plt.show()

# %% [markdown]
# ## Plot a normal probability plot

# %%
sns.set_theme()
fig, ax = plt.subplots()
res = probplot(x=plasma["Level"], plot=ax)
plt.show()

# %% [markdown]
# ## Commentary
#
# The points lie roughly along a straight-line.
# This suggests a normal model is plausible for the blood plasma nicotine levels of smokers.
