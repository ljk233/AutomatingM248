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
# # Linear regression
#
# **date** : 2021-05-03
#
# **aim** : Fitting a linear regression model
#
# **reference:** M248, Computer book C, chapter 2
#
# **packages** : `scipy`

# %% [markdown]
# ## 1. Setup the notebook

# %%
from src import load
from src.linregr import LinearRegression
# from scipy.stats import linregress, probplot, t
import seaborn as sns
import matplotlib.pyplot as plt

# %%
# set seaborn theme
sns.set_theme()

# %% [markdown]
# ## 2. Fitting a linear regression model I
#
# **aim** : Estimate the least squares line for Age (explanatory) against Cholesterol (response).
#
# **reference** : activity 3
#
# **data** : cholesterol.csv
#
# **description** : The sample contains data on the total cholesterol levels measured for 11 individuals aged over 40 years.

# %% [markdown]
# ### 2.1 Import the data

# %%
sample = load.cholesterol()
x = sample["Age"]  # explanatory
y = sample["Cholesterol"]  # response

# %% [markdown]
# ### 2.2 Model the relationship

# %%
# declare and initialise
model = LinearRegression(x=x, y=y)

# %%
# initialise the model
model.fit()

# %% [markdown]
# ### 2.3 Report on the model

# %%
model.report()

# %% [markdown]
# ### 2.4 Discussion
