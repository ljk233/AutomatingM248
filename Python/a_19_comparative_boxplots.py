
# =============================================================================
# References
# ==========
#
# - Computer activity A.19
# - Comparative boxplots (HB.p5; U1.5.3; CA4.3)
# - Plot multiple boxplots as a comparative boxplot
# =============================================================================

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# import the data
df = pd.read_csv("./data/response-inhibition.csv")

# preview the DataFrame
df.head()

# =============================================================================
# Light data transformation to recast the categorical data
# =============================================================================

# Recast Group -> cat
df = df.astype({'Group': 'category'})

# recode Groups to Treatment, Control
df['Group'].replace({0: 'Control', 1: 'Treatment'}, inplace=True)

df.head()

# =============================================================================
# Output multiple horizontal boxplots by specifying y as the grouping
# =============================================================================

f, ax = plt.subplots()

sns.boxplot(data=df,
            x="Weight change",
            y="Group")

plt.show()

# =============================================================================
# Output multiple vertical boxplots, simply swap x for y
# =============================================================================

f, ax = plt.subplots()

sns.boxplot(data=df,
            y="Weight change",
            x="Group")

plt.show()
