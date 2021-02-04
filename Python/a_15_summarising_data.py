
# =============================================================================
# References
# ==========
#
# Computer activity A.14
#
# Summarising data
# - Sample mean (HB.pp6; U1.4.1; CA3).
# - Sample median (HB.pp6; U1.4.1; CA3).
# - Sample quartiles (HB.pp6; U1.4.1; CA3).
# - Sample IQR (HB.pp6; U1.4.1; CA3).
# - Sample standard deviation (HB.pp6; U1.4.1; CA3).
#
# Use Pandas to calculate numerical summaries of some data.
#
# This differs to Computer Activity 14 because here we need to
# subcategorise the data.
# =============================================================================

import pandas as pd

# import the data
df = pd.read_csv("./data/response-inhibition.csv")

# preview the DataFrame
df.head()

# =============================================================================
# aggregate the data
# =============================================================================

# check dtypes
df.dtypes

# Recast Group -> cat
df = df.astype({'Group': 'category'})

# recode Groups to Treatment, Control
df['Group'].replace({0: 'Control', 1: 'Treatment'}, inplace=True)

df.head()

# =============================================================================
# Data is merged. Use groupby() to stratify the data
# =============================================================================

# Select Groups, Weight Change, and then Groupby
df_grouped = df[['Group', 'Weight change']].groupby("Group")

# =============================================================================
# Output default descriptive table.
# =============================================================================

df_grouped.describe()

# =============================================================================
# Return individual summary measures.
# =============================================================================

# sample mean
df_grouped.mean()

# sample median
df_grouped.median()

# lower sample quartile
df_grouped.quantile(0.25)

# upper sample quartile
df_grouped.quantile(0.75)

# Sample iqr
df_grouped.quantile(0.75) - df_grouped.quantile(0.25)

# sample standard deviation
df_grouped.std()
