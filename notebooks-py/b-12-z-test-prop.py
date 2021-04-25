# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:hydrogen
#     text_representation:
#       extension: .py
#       format_name: hydrogen
#       format_version: '1.3'
#       jupytext_version: 1.11.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # One-sided z-test for a proportion
#
# **date:** 2021-04-17
#
# **aim:** Perform a two-sided **z-test** with one sample of data.
#
# **reference:** Computer book B, Activity 26
#
# **module:** `statsmodels.stats.proportion.proportions_ztest`

# %% [markdown]
# ## Setup

# %%
from statsmodels.stats.proportion import proportions_ztest

# %% [markdown]
# ## Hypotheses
#
# The Labour Force Survey (ONS, 2014) of 254 young people aged between 20 and 34 years living in Wales found that 68 were still living at home with their parents.
# Previous surveys had found the same proportion to be one in every four young adults.
#
# Let the hypotheses be
#
# $$
# H_{0} : p_{W} = 0.25, \> p_{W} \neq 0.25
# $$
#
# where the variable $p_{W}$ is the proportion of young adults between 20 and 34 years living with their parents in Wales in 2014.

# %% [markdown]
# ## Results

# %%
proportions_ztest(
    count=68,
    nobs=254,
    value=0.25,
    prop_var=0.25
)
