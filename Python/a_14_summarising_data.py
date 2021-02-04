
# =============================================================================
# References
# ==========
#
# Computer activity A14
#
# Summarising data
# - Sample mean (HB.pp6; U1.4.1; CA3).
# - Sample median (HB.pp6; U1.4.1; CA3).
# - Sample quartiles (HB.pp6; U1.4.1; CA3).
# - Sample IQR (HB.pp6; U1.4.1; CA3).
# - Sample standard deviation (HB.pp6; U1.4.1; CA3).
#
# Use Pandas to calculate numerical summaries of some data.
# Output comparative boxplots of the data.
# =============================================================================

import pandas as pd

# import the data
df = pd.read_csv("./data/response-inhibition.csv")

# preview the DataFrame
df.head()

# check dtypes
df.dtypes

# =============================================================================
# output a simple table of summary measures
# =============================================================================

# output a simple table of summary measures
df["Weight change"].describe()

# =============================================================================
# Return individual summary measures.
# =============================================================================

# sample mean
df["Weight change"].mean()

# sample median
df["Weight change"].median()

# lower sample quartile
df["Weight change"].quantile(0.25)

# upper sample quartile
df["Weight change"].quantile(0.75)

# sample IQR
df["Weight change"].quantile(0.75) - df["Weight change"].quantile(0.25)

# sample standard deviation
df["Weight change"].std()
