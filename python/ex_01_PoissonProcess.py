
##############################################################################
# Aim of the workbook is plot the data in goals.csv
##############################################################################

import pandas as pd
from scipy.stats import poisson, norm
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# import the data
df = pd.read_csv("./data/goals.csv")

df.head()

# minute is a string, swap 45+ and 90+ for 90, then recast to int
df["minute"].replace(["45+", "90+", "120+"], [45, 90, 120], inplace=True)
df = df.astype({'minute': 'int64'})

df.dtypes

# drop goals in extra time
df = df.query('minute < 90').copy(False)

# game_id is disjointed. Create an id key
id = pd.DataFrame(data=df["game_id"])
id = id.drop_duplicates().copy(False)
id["game_key"] = np.arange(start=0, stop=id["game_id"].size)
id.reset_index(inplace=True, drop=True)

# map in id
df = df.join(on=df["game_id"],
             other=id.set_index("game_id"))

df.head()

##############################################################################
# Visualisations
##############################################################################

##############################################################################
# Number of goals per game
##############################################################################

s_count = df.groupby("game_id")["game_id"].count()

f, ax = plt.subplots()
sns.set_theme(style="darkgrid")

sns.countplot(x=s_count,          # set the x-axis
              color="royalblue")    # set the colour

ax.set(title="Number of Goals per Game",               # set the title
       xlabel="Number of goals",    # set x-label
       ylabel="Frequency")          # set y-label

plt.show()

##############################################################################
# Rate of occurrence
##############################################################################

# add goal_id, add running_time
df["goal_id"] = np.arange(start=1, stop=df["game_id"].size+1)
df["running_time"] = (df["game_key"])*90 + df["minute"]

f, ax = plt.subplots()

sns.scatterplot(data=df,
                x="running_time",
                y="goal_id",
                color="royalblue")

ax.set(title="Rate of Occurrence of a Goal Scored",               # set the title
       xlabel="Running Time",    # set x-label
       ylabel="Goal")          # set y-label

plt.show()

##############################################################################
# Waiting time between goals
##############################################################################

# calculate the time between successive goals
df["waiting_time"] = df["running_time"] - df["running_time"].shift(1)
# replace the NaN in waiting_time
df["waiting_time"].replace(np.nan, 0, inplace=True)

f, ax = plt.subplots()

sns.histplot(data=df,
             x="waiting_time",            # set bins to width 1
             edgecolor="none",       # set density
             color="royalblue")

ax.set(title="Rate of Occurrence of a Goal Scored",               # set the title
       xlabel="Running Time",    # set x-label
       ylabel="Goal")          # set y-label

plt.show()

##############################################################################
# Check mean and var for number of goals per game
##############################################################################

s_count.mean()
s_count.var()

##############################################################################
# Check mean and sd of waiting time
##############################################################################

df["waiting_time"].mean()
df["waiting_time"].std()

##############################################################################
# Estimate the paramter mu
##############################################################################

# average goals per game
mean = s_count.mean()
std = s_count.std(ddof=1)

##############################################################################
# Interval estimate for mean
##############################################################################

a_dist = poisson(mean)

z = norm(mean, std)
z.interval(0.95)

z
mean + z*(mean/df["waiting_time"].size)**0.5
mean - z*(mean/df["waiting_time"].size)**0.5
