
# README

This project includes a series of visualisation and hypotheses testing about the English Premier League.

I think I'm too focused on recreating the data.
I should instead focus on just processing the data!

## TO-DO

- [ ] Add doc explaining source data
- [ ] Refactor notebooks/setup
  - There could be an argument to remove them completely?

## NOTEBOOKS

The notebooks folder contains two sub-folders, each dealing with a different area of concern.

Notebooks in the top-levels `notebooks/` folder contain finished reports.

**1_setup**
: contains a series of notebooks that will recreate the  processed data sets in out, so long as the source file is saved in the **data/in** sub-folder.

**2_exploration**
: contains a series of notebooks that are concerned with exploring the data set.
These act as staging grounds for the building of the support classes in **src** which are used in the **3_final** notebooks.
*They should be considered to be unstable.*

## References

--**Add source**

## Ideas

- Home team is more likely to score fist
  - Need data: `game`, `first_goals`, `team`
- Teams are conceding more goals
  - Average Goals score 2018/19 = Average Goals score 2019/20
- Covid and loss of the home of the home team advantage
  - Proportion Home wins (201819) = Proportion Home wins (2020/21)
  - Missing data 2020/21

## Future

- Plans to spin this off into part of a larger **Statistical Analysis** GH-repo.
- Think about how you would refactor the folder structure to make it more sensible.
