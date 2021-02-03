
# =============================================================================
# References
# ==========
#
# - Computer activity 11 and Computer activity 12
# - Boxplots (HB.p5. U1.3.3. CA2.2.)
# - Plot a boxplot.
# =============================================================================

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# import the data
df = pd.read_csv("./data/membership.csv")

# preview data
df.head()

# =============================================================================
# Plot a horizontal boxplot
# =============================================================================

f, ax = plt.subplots()

sns.boxplot(data=df,
            x="Percentage",
            color="royalblue")

plt.show()

# =============================================================================
# Plot a vertical boxplot by changing why parameter references the data
# =============================================================================

f, ax = plt.subplots()

sns.boxplot(data=df,
            y="Percentage",
            color="royalblue")

plt.show()
