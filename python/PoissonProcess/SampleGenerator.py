
##############################################################################
# Goal
# ====
# Create a sample of dates and times that model the receipt
# of emails into an email inbox.
##############################################################################

import pandas as pd
from scipy.stats import expon, poisson, randint
from math import floor

##############################################################################
# Set the parameter
##############################################################################

# select random integer between 5 and 15 the average per hour
mu = randint.rvs(low=5, high=16)
days = 5  # the days covered by the sample

##############################################################################
# Generate the sample
##############################################################################

working_hours = 8*days # the number of hours in the sample

sample = pd.DataFrame()

# Generate a sample of 10000
sample["interval"] = expon.rvs(loc=0, scale=1/mu, size=10000)

# Add cumulative sum of interval
sample["running_total"] = sample["interval"].cumsum()

# Take a subsample for the desired number of days
# Note the @ annotation for passing the local variable
subsample = sample.query("running_total < @working_hours").copy(deep=False)

subsample.head()

##############################################################################
# From the running running_total, get the datetime
##############################################################################

START_DATE = pd.to_datetime(["2021-02-08"], format="%Y-%m-%d")

subsample["hour"] = pd.to_timedelta(subsample["running_total"], unit="h")

subsample
