
"""
Large-sample approximate confidence intervals for population means
    See <> for the full write-up of the report in r.

date
: 2021-04-16

reference
: Computer book B, Activity 15

desc
: Calculate large-sample confidence intervals for a population mean
from a sample of data

data
: glass-fibres.csv
"""

###
# Setup
#

from setup import load
from statsmodels.stats.weightstats import zconfint
import seaborn as sns
import matplotlib,pyplot as plt

# import the data and assign local var
fibres = load.glass_fibres()
str = fibres["Strength"]

###
# About
#

# preview the data
fibres.head()

# summarise the data
str.describe()

# visualise the data
sns.histplot(x=str, binwidth=0.2)

###
# Results
#

# 90%CI: population mean
zconfint(x1=str, alpha=0.1)
