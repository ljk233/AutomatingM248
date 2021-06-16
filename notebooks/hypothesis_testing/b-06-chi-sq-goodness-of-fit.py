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
#     display_name: Python 3.8
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Chi-square goodness-of-fit test
#
# **date** : 2021-04-18
#
# **aim** : Perform a **chi-square** goodness-of-fit test.
#
# **reference** : N/A

# %% [markdown]
# ## 1. Setup the notebook

# %%
from src import load
from scipy.stats import chisquare
import seaborn as sns
import matplotlib.pyplot as plt

# %% [markdown]
# ## 2. Chi-square goodness-of-fit test
#
# **aim** : Analyse whether it is reasonable to claim that the total number of goals scored per ten minute period in a football game is unifomally distributed across all nine periods.
#
# **data** : uniform_goal.csv
#
# **description** : Data on the total number of goals scored per ten minute period in an English Premier League football season in normal time in season 18-19.

# %% [markdown]
# ### 2.1 Import the data

# %%
# import the data
goals = load.uniform_goals()

# %%
# assign local vars
group = goals["group"]
obs = goals["obs"]

# %% [markdown]
# ### 2.2 Visualise the data

# %%
sns.barplot(data=goals, x="group", y="obs", color="cornflowerblue")
plt.show()

# %% [markdown]
# ### 2.3 Perform the test

# %%
chisquare(f_obs=obs)

# %% [markdown]
# ### 2.4 Plot the results of the test
#
# Plot a side-by-side bar chart showing the **observed** and **expected** number of goals.
#
# Expected number of goals is **n Pr,** here **n** is the total number of goals scored in the observatation, and **Pr** is the probability of a goals being scored in a particular group.
# As the proposed distribution is a **discrete uniform,** each grouping should have the same probability of an event.
# There are nine groups.

# %%
pr = 1/9  # probability goal is scored
n = obs.sum()  # goals scored in period

# %%
# add expected goals to dataframe
goals["exp"] = n*pr

# %%
# melt the data into long format
mgoals = goals.melt(id_vars="group", value_vars=["obs", "exp"])

# %%
f, ax = plt.subplots()
ax = sns.barplot(data=mgoals, x="group", y="value", hue="variable")
plt.legend(bbox_to_anchor=(1.20, 1))    # move legend outside axis
plt.show()

# %% [markdown]
# ## Discussion
#
# Give that $p \in (0.01, 0.05]$, there is moderate evidence against the null hypothesis that the distribution of goals across the 90 minutes of a football match are uniformally distributed.
# There is moderate evidence to support the claim that the total number of goals scored per ten minute period in an EPL football game are not uniformally distributed.
