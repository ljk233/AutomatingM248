
"""
"Large-sample confidence intervals: proportions"

date
: 2021-04-21

aim
: Calculate a **100(1-a)%** approximate confidence interval for a proportion

reference
: M248 Computer book B, Activity 18

data:
: accidents.csv

description
: Number of accidents suffered by each of 414 machinists over a period of time
"""

###
# Setup
#

from setup import load
from statsmodels.stats.proportion import proportion_confint
import seaborn as sns
import matplotlib.pyplot as plt

# import the data and assign local vars
accidents = load.accidents()
# count number of entries where accidents != 0
x = accidents.query('Accidents != 0').count()[0]
# count the number of rows in totals
n = accidents["Accidents"].size

###
# About
#

# preview the data
accidents.head()

# summarise the data
accidents.describe()

# visualise the data
sns.countplot(x=accidents["Accidents"], color="cornflowerblue")
plt.show()

###
# Results
#

# 99% CI: proportion of workers who suffered at least one accident
proportion_confint(count=x, nobs=n, alpha=0.01)
