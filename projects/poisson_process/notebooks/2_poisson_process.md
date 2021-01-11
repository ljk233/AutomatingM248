---
jupyter:
  jupytext:
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.9.1
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

# 2. Data preparation for the Poisson process

In this notebook, we process the raw data to produce meaningful analysis.

In section 1, we import that data, check and recast the `dtypes`, and then process the date and time of each email.

```python
from scipy.stats import poisson, expon, norm, bernoulli
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from datetime import datetime
from math import sqrt
```

## 1. Data import and preparation

The date needs to be wrangled so we can answer the questions.

```python
# load the dataset
df = pd.read_csv("email_log.csv")
```

```python
df.head()
```

```python
df.dtypes
```

The **DATE** and **TIME** attributes have come through as `objects`.
Let us recast them to `datetime64`.

```python
# convert the DATE and TIME to DATETIME
df["DATE"] = pd.to_datetime(df["DATE"])
df["TIME"] = pd.to_datetime(df["TIME"])
```

```python
df.head()
```

```python
df.dtypes
```

The Poisson process works in continuous time.
However, there are gaps in the data (between 5pm and 9am).

Let us introduce some new fields so we can measure the data in continuous time.

- **DAY**
  - As `int`, a count from in the days since the origin date.
- **HOUR**
  - As `int`, the hour the email is received with range $(0, 7)$, so
    - 9am $\to$ 0
    - 10am $\to$ 1
    - $\dots$
- **MINUTE**
  - As `int`, the minute the email is received.
- **SECOND**
  - As `int`, the seconds the email is received.

```python
# set the origin data
START_DAY = pd.to_datetime("2020-01-01")

# subtract the origin from the current date
df["DAY"] = df["DATE"] - START_DAY
```

```python
df.dtypes
```

**DAY** is now of dtype `timedelta64`.
Recast in to `int64` so we can manipulate it for calculations.

```python
# recast DAY
df["DAY"] = df["DAY"].dt.days.astype('int64')

# get TIME.hour of TIME as int
df["HOUR"] = df["TIME"].dt.hour.astype('int64')

# reindex 9.00-17.00 to 00.00-08.00
df["HOUR"] = (df["HOUR"] - 1) % 8

# recast TIME.minute to int
df["MINUTE"] = df["TIME"].dt.minute.astype('int64')

# recast TIME.second to int
df["SECOND"] = df["TIME"].dt.second.astype('int64')
```

```python
df.head()
```

```python
df.dtypes
```

**TIME** is set to today's date due to the way `pandas` handles `datetimes`.
This is safe to ignore.
The data is now ready.

## 2. Number of emails per hour

Let us create a new view of the data that has the following attributes:

- $X$: The number of emails received in an hour.
- $f$: The frequency of $X$.

```python
# add a key: dd-hh
df["KEY"] = df["DAY"].astype("str") + "-" + df["HOUR"].astype("str")

# group-by KEY, and count the rows that posses the KEY
v_emails_per_hour = df.groupby(by=["KEY"]).count()
v_emails_per_hour.reset_index(inplace=True)
```

Let us tidy up the view to make it more legible.
(This is optional).

```python
# columns to drop
v_emails_per_hour.drop(columns=["DATE",
                                "TIME",
                                "DAY",
                                "MINUTE",
                                "SECOND"],
                       inplace=True)

# rename column
v_emails_per_hour.rename(columns={"HOUR": "X"}, inplace=True)
```

```python
v_emails_per_hour.head()
```

We now have the count of emails received per hour, $x_{i} \in X$, so let us count each occurence of $x_{i}$.

```python
v_number_of_emails = v_emails_per_hour.groupby(by="X").count()

# rename the column
v_number_of_emails.rename(columns={"KEY": "f"}, inplace=True)

# reset the index
# this ungroups the email so we can plot the data
v_number_of_emails.reset_index(inplace=True)
```

Let us again tidy up the view.
(This is again optional).

```python
v_number_of_emails.head()
```

Plot the histogram.

```python
sns.barplot(data=v_number_of_emails,
            x="X",
            y="f",
            color="royalblue")
plt.show()
```

Let us `describe()` the `DataFrame`, an then declare reference variables for the mean and variance.

```python
v_emails_per_hour.describe()
```

```python
mean_number = v_emails_per_hour["X"].mean()
```

```python
# use ddof=1 so we calculate the sample var
var_number = v_emails_per_hour["X"].var(ddof=1)
```

## 3. Rate of emails remains constant

We need to produce a simple "TIME RECEIVED" against "EVENT" scattergraph.
Let us first get the timestamp (in hours passed since the origin).

First we convert each of **DAY**, **MINUTE**, and **SECOND** into unit decimal hours.

```python
v_rate_of_emails = pd.DataFrame()

# Declare constants
HOURS_PER_DAY = 8  # There are 8 hours in a working day.
HOURS_PER_MINUTE = 1 / 60  # A minute is 1/60 hours
HOURS_PER_SECONDS = 1/3600  # A second is 1/3600 hours

# Transfrom the attributes
v_rate_of_emails["DAY (HH)"] = df["DAY"] * HOURS_PER_DAY
v_rate_of_emails["HOUR (HH)"] = df["HOUR"]
v_rate_of_emails["MINUTE (HH)"] = df["MINUTE"] * HOURS_PER_MINUTE
v_rate_of_emails["SECOND (HH)"] = df["SECOND"] * HOURS_PER_SECONDS
```

We can now find the hours passed since the origin (in hours) by summing the four new attributes.

```python
v_rate_of_emails["TIME (HH)"] = (v_rate_of_emails["DAY (HH)"] +
                                 v_rate_of_emails["HOUR (HH)"] +
                                 v_rate_of_emails["MINUTE (HH)"] +
                                 v_rate_of_emails["SECOND (HH)"])
```

```python
v_rate_of_emails.head()
```

Let us add an event label to the view.
This will be the data plotted on the $y-$axis.

```python
# get size of DataFrame
length = v_rate_of_emails["TIME (HH)"].size + 1

# create the series
a_range = np.arange(start=1, stop=length, step=1)

# append a_range to tmp
v_rate_of_emails["EVENT"] = a_range
```

Tidy up the view.
(This is optional).

```python
v_rate_of_emails.drop(columns=["DAY (HH)",
                               "HOUR (HH)",
                               "MINUTE (HH)",
                               "SECOND (HH)"],
                      inplace=True)
```

```python
v_rate_of_emails.head()
```

Plot the time series.

```python
sns.scatterplot(data=v_rate_of_emails,
                x="TIME (HH)",
                y="EVENT",
                alpha=1,
                s=1)
plt.show()
```

## 4. Waiting time between emails

We'll make use of the view from the rate of emails section, introducing a new attribute that measures the time past (in hours) between successive events.

The `shift()` method to compare successive time stamps.

```python
v_waiting_times = (v_rate_of_emails["TIME (HH)"] -
                   v_rate_of_emails["TIME (HH)"].shift(1))

# first entry will be NaN, as there is nothing to compare it with.
v_waiting_times.dropna(inplace=True)
```

Let us plot a histogram of the waiting times.

The parameter `bins=50` was used to make the plot more sensible, as the `Seaborn` default chose an extremely small bin range.

```python
sns.histplot(data=a_waiting_time, stat="probability", bins=50)
plt.show()
```

Let us `describe()` the `DataFrame`, an then declare reference variables for the mean and variance.

```python
a_waiting_time.describe()
```

```python
mean_waiting = a_waiting_time.mean()
```

```python
std = a_waiting_time.std(ddof=1)
```

## 5. Point estimate of $\lambda$

The maximumum likelihood estimator for the Poisson parameter $\widehat \lambda_{X}$ is

$$
\widehat \lambda_{X} = \overline X,
$$

and the MLE for the exponential parameter $\widehat \lambda_{T}$ is

$$
\widehat \lambda_{T} = \frac{1}{\overline T}.
$$

It should be that $\widehat \lambda_{X} \approx \widehat \lambda_{T}$.

We have two ways to estimate it here: The number of emails per hour and the waiting time between emails.
Let us calculate it using both datasets.

We have already calculated the expected number of emails per hour.

```python
mean_number
```

Therefore, we propose that $\widehat \lambda_{X}$ is approximately 13.6.

```python
rate_number = mean_number
```

We have also already calculated the expected waiting time between emails.

```python
mean_waiting
```

Therefore, we propose that $\widehat \lambda_{T}$ is approximately...

```python
rate_waiting = 1 / mean_waiting
rate_waiting
```

## 6. Confidence interval for $\lambda$

We now need some parameters:

- $\overline x$
- $z$
- $n$

```python
# get z
z = round(norm().ppf(q=0.975), 3)
z
```

```python
# get n
n = v_emails_per_hour.index.values.size
n
```

Calculate the confidence interval

```python
norm(loc=mean_number, scale=sqrt(mean_number/n)).interval(0.95)
```
