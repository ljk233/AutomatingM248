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
# # Exact confidence intervals: difference between two normal means
#
# date: 2021-04-16
#
# aim: Calculate a 100(1-a)% exact confidence interval for the difference
# between two normal means.
#
# reference: Computer book B, Activity 22
#
# data: skulls.csv
#
# description: Maximum skull breadth (in mm) of 84 skulls of Etruscan males and 70 skulls of modern Italian males.
#
# modules: `scipy`

# %% [markdown]
# ## Setup

# %%
from setup import load
from scipy.stats import t, probplot
from math import sqrt
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# %%
def get_dof(a, b) -> int:
    """
    Calculates the degrees of freedom of two samples.
    @params a,b
        array-like objects
    """
    return a.size + b.size - 2


# %%
def get_ese(a, b) -> float:
    """
    Calculates the estimated standard error of two samples.
    @params a,b
        array-like objects
    """
    # pooled_var
    num = ((a.size - 1) * a.var() + (b.size - 1) * b.var())
    denom = get_dof(a, b)
    pooled_var = num/denom
    return sqrt(pooled_var) * sqrt(1/a.size + 1/b.size)


# %%
# import the sample
skulls = load.skulls()

# %%
# declare local vars
etr = skulls["Etruscans"].dropna()
ita = skulls["Italians"].dropna()

# %% [markdown]
# ## Visualise

# %%
skulls.plot(kind="box")
plt.show()

# %% [markdown]
# ## Calculate a 100(1-a)% confidence interval

# %% [markdown]
# ### Check assumptions

# %%
# check normality using normal probability plots
sns.set_theme()
f, [ax1, ax2] = plt.subplots(nrows=1, ncols=2, sharey=True)
ax1 = probplot(x=etr, plot=ax1)
ax1 = probplot(x=ita, plot=ax2)
plt.show()

# %% [markdown]
# Add commentary

# %% [markdown]
# ### Check for common variance

# %%
if etr.var() > ita.var():
    print(etr.var()/ita.var())
else:
    print(ita.var()/etr.var())

# %% [markdown]
# ### Return the confidence interval

# %%
# get difference, degree of freedom, and estimated stand error
# included for clarity
dof = get_dof(etr, ita)
diff = etr.mean() - ita.mean()
ese = get_ese(etr, ita)

# %%
# calculate the ci
t.interval(
    alpha=0.95,
    df=dof,
    loc=diff,
    scale=ese)
