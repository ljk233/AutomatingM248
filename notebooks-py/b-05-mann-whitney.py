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
# # Mann-Whitney test
#
# **date** : 2021-04-17
#
# **aim** : Perform a **Mann-Whitney Test**.
#
# **reference:** M248, Computer book B, chapter 11
#
# **packages** : `scipy`

# %% [markdown]
# ## 1. Setup the notebook

# %%
from src import load
from scipy.stats import mannwhitneyu
import seaborn as sns
import matplotlib.pyplot as plt

# %% [markdown]
# ## 2. The Mann-Whitney test
#
# **aim** : Test the hypothesis $H_{0} : \ell = 0, \> \ell \neq 0$, where $\ell$ is the underlying population difference in location between the patients deemed psychotic and those deemed non-psychotic. (See description.)
#
# **reference** : activity 37 (*amended*)
#
# **data:** dopamine.csv
#
# **description:** Data on the dopamine $\beta$-hydroxylase enzyme activity in samples of cerebro-spinal fluid (in **nmol/(ml)(h)/mg**) taken from 25 hospitalised patients with schizophrenia who were treated with antipsychotic medication, who after a period of time were classified as either psychotic or non-psychotic by hospital staff.

# %% [markdown]
# ### 2.1 Import the data

# %%
# import the data
dopamine = load.dopamine()

# %%
# assign local vars
non_psy = dopamine["Non-psychotic"].dropna()
psy = dopamine["Psychotic"].dropna()

# %% [markdown]
# ### 2.2 Visualise the data

# %%
ax = sns.boxplot(data=dopamine.melt(), x="value", y="variable")
ax.set(xlabel="Dopamine level", ylabel="Patient type")
plt.show()

# %% [markdown]
# ### 2.3 Perform the Mann-Whitney test
#
# Note that `"two-sided"` should be passed as the actual argument for `alternative`, given the default is `None`.
# We can return values unadjusted for ties by passing `True` as an actual argument for `use_continuity`.

# %% [markdown]
# ### Calculations

# %%
mannwhitneyu(x=psy, y=non_psy, alternative="two-sided")
