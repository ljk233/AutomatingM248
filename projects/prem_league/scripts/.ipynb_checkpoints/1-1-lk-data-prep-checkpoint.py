"""
date:
    2021-04-10
data:
    /projects/prem_league/data/in/epl_1819.csv
"""

"""
home_team_goal_count
away_team_goal_count
total_goal_count
total_goals_at_half_time
home_team_goal_count_half_time
away_team_goal_count_half_time
home_team_goal_timings
away_team_goal_timings
"""

import pandas as pd
import numpy as np
from scipy.stats import poisson, expon
import seaborn as sns


def game_status(home: int, away: int) -> str:
    """
    Identifies which team won a game.
    Compares the goals scored, returning with "H", "A", "D" as appropriate.
    """

    if home>away:
        return "home"
    elif away<home:
        return "away"
    else:
        return "draw"


source = pd.read_csv("../data/in/epl_1819.csv")
# get interesting columns
goal_timings = source[[
    "home_team_goal_count",
    "away_team_goal_count",
    "total_goal_count",
    "total_goals_at_half_time",
    "home_team_goal_count_half_time",
    "away_team_goal_count_half_time",
    "home_team_goal_timings",
    "away_team_goal_timings"
]]
# preview the df
goal_timings.head()

# ============================================================================
# Poisson process 1: X is goals_per_game
# ============================================================================

goal_timings["total_goal_count"].describe()

# plot the number of goals per game
sns.countplot(data=goal_timings, x="total_goal_count")

# plot Poisson(mu)
poiss = poisson(2.8)
# declare range
r = np.arange(start=0, stop=9)
# plot the pmf
sns.barplot(x=r, y=poiss.pmf(r))

# ============================================================================
# Poisson process 2: W is intervals between goals
#   - We need unpack the data into long format
#   - game_id, status (who won), goal_time
# ============================================================================

# generate game_id
game_id: list = np.arange(
    start=1,
    stop=goal_timings["home_team_goal_count"].size +1
)

# identify status:who won the game? H/A/D?
status = game_status(
    goal_timings["home_team_goal_count"],
    goal_timings["away_team_goal_count"]
)
