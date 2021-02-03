
# =============================================================================
# References
# ==========
#
# - No corresponding activity
# -
#
# Suppose that a continuous variable X can only take values in the range 0:2.
# It has a p.d.f.
#
# f(x) = (5-x)/8
#
# - Confirm it is a valid p.d.f.
# - Calculate F(1.5)
# - Calculate E(X)
# - Calculate V(X)
# - Plot the p.d.f.
# =============================================================================

from scipy.integrate import quad
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# =============================================================================
# Declare functions
# =============================================================================


def f(x: float):
    return (5-x)/8


def xf(x: float):
    return x * f(x)


def x2f(x: float):
    return x**2 * f(x)


a = 0  # lower
b = 2  # upper

# =============================================================================
# Declare a pd.DataFrame
# =============================================================================

pdf = pd.DataFrame()
pdf["X"] = np.linspace(start=0, stop=2, num=100)
pdf["f"] = pdf["X"].apply(f)
pdf.head()

# =============================================================================
# Confirm valid p.d.f.
# Expect both to return to True.
# =============================================================================

# Integrates to 1 over range
quad(func=f, a=a, b=b)[0] == 1

# All Pr > 0. Count rows where Pr <= 0
pdf.query('f <= 0')["f"].count() == 0

# =============================================================================
# Calculate the F(1.5)
# =============================================================================

quad(func=f, a=a, b=1.5)[0]

# =============================================================================
# Calculate E(X).
# =============================================================================

mu = quad(func=xf, a=a, b=b)[0]
mu

# =============================================================================
# Calculate V(X)
# =============================================================================

var = quad(func=x2f, a=a, b=b)[0] - mu**2
var

# =============================================================================
# Plot the p.d.f.
# =============================================================================

fig, ax = plt.subplots()

x = np.linspace(start=0, stop=2, num=10000)  # declare the range of X

sns.lineplot(x=x,  # x-axis
             y=np.array(f(x)),  # calaculate Pr(X)
             color="royalblue")

plt.show()
